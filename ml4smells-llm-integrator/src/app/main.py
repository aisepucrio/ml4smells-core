from application.dtos.message_operation_input import MessageOperationInput
from application.usecase.llm_operation_usecase import LLMOperationUseCase
from infrastructure.external_service.consume_message import ConsumeMessage

import json
from pathlib import Path
from typing import List
import time 

BATCH_SIZE = 50
FALTANTES_PATH = Path("faltantes.json")


def process_message(message):
    message_input = MessageOperationInput.from_raw(message)
    
    gemma_service = LLMOperationUseCase()
    gemma_service.llm_operation_use_case(message_input)

    if "error" in message:
        raise ValueError("Error processing the message.")


def create_line_queue(file_path: Path) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_batch_from_queue(queue: List[str], batch_size: int):
    for i in range(0, len(queue), batch_size):
        yield queue[i:i + batch_size]

def process_batch(batch: List[str]):
    for line in batch:
        try:
            msg = json.loads(line)
            process_message(msg)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar linha: {line}\nErro: {e}")

def save_remaining_lines(lines: List[str], path: Path):
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')
    print(f"\n❗ Linhas restantes salvas em '{path}'")

def run_batch_processing(file_path: Path):
    if not file_path.exists():
        print(f"O arquivo '{file_path}' não existe.")
        return

    # Se houver um arquivo de faltantes, começamos dele
    if FALTANTES_PATH.exists():
        print(f"⚠️ Encontrado arquivo de faltantes: {FALTANTES_PATH}")
        line_queue = create_line_queue(FALTANTES_PATH)
    else:
        line_queue = create_line_queue(file_path)

    print(f"Total de linhas a processar: {len(line_queue)}")

    try:
        while line_queue:
            for line_batch in get_batch_from_queue(line_queue, BATCH_SIZE):
                print(f"\n🔄 Processando batch com {len(line_batch)} linhas")

                try:
                    process_batch(line_batch)
                except Exception as e:
                    print(f"❌ Erro durante processamento do batch: {e}")
                    raise e  # ainda queremos cair no finally

                # Remove as linhas processadas da fila
                line_queue = line_queue[len(line_batch):]
                print(f"✔️ Restam {len(line_queue)} linhas na fila")

    except (KeyboardInterrupt, Exception) as e:
        print(f"\n⚠️ Execução interrompida: {e}")
    finally:
        if line_queue:
            save_remaining_lines(line_queue, FALTANTES_PATH)
        else:
            if FALTANTES_PATH.exists():
                FALTANTES_PATH.unlink()  # remove arquivo se tudo foi processado
            print("\n✅ Todas as linhas foram processadas com sucesso!")

def main():    
    # consume = ConsumeMessage()
    # consume.get_message(process_message)

    run_batch_processing(Path("./codes/deepseek1_5b__long_parameter_list_cot_and_zero_shot_with_ast_and_without_ast.json"))


if __name__ == "__main__":
    main()
