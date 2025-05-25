<div align="center" >
    <img src="docs/img/background.png" width="600px" style="border-radius:10%;"/>
    </br>
    <h3>LLM Integrator</h3>
</div>

This application is designed to seamlessly integrate with Language Learning Models (LLMs) through an Ollama instance or REST. The goal is to provide integration with LLMs in a scalable, flexible, and efficient manner. The application serves as middleware, facilitating communication between various client systems and the LLMs.

# Built with
* [Python 3.10](https://www.python.org/downloads/release/python-3100/)
* [Ollama](https://ollama.com/)
* [RabbitMq](https://www.rabbitmq.com/)


# Project Structure

```
├──📁 ml4smells-llm-integrator
│   ├──📁 docs
│   ├──📁 src
│   |   ├──📁 app
│   |   |   ├──📁 application
│   |   |   └──📁 infrastucture
│   ├──📄 changelog
│   ├──📄 .gitignore

```

# How to run?

* 1 - Make sure you are in the `app` folder
* 2 - Run `pip install -r requirements.txt`
* 3 - Create: `.env`
* 4 - Set up [RabbitMQ](https://www.rabbitmq.com/docs/download) according to the `.env` file
* 5 - Run Ollama with the models you intend to use
* 6 - Run `python main.py`


# Dependencies 

* RabbitMq
* Ollama
