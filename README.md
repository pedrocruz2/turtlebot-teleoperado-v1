# Controle do TurtleBot com ROS 2

Este projeto contém um nó ROS 2 para controlar um TurtleBot utilizando entradas do teclado. O nó é capaz de verificar se o robô está inicializado e pronto para receber comandos antes de enviá-los. Além disso, inclui um serviço para parar o robô e finalizar o processo.

## Pré-requisitos

- Python
- Pip
- Ros2
- Ter um TurtleBot3 conectado com a raspberry-pi e o ros configurado (Ou simular via gazebo ou webots)
### Clonagem do Repositório E Instalações das dependências

Clone o repositório do projeto:
```sh
git clone https://github.com/pedrocruz2/turtlebot-teleoperado-v1/
```
Navegue para o Diretório do projeto: 
```sh
cd turtlebot-teleoperado-v1/
```
Instale todas as dependências: 
```sh
pip install -r requirements.txt
```
### Rodar o Projeto
Para rodar o projeto você deve executar o arquivo ``` key_listener.py``` utilizando o comando:
```sh
python3 key_listener.py
```
Se tudo foi feito corretamente, você pode controlar o robô utilizando as teclas W (CIMA), A (BAIXO), S (DIREITA), D (ESQUERDA) e utilizar X ou Ctrl+C para parar o robô. Além disso, você pode externamente parar o funcionamento do robô rodando o arquivo ```robot_killer.py```




