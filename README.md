# Terravoice
Crie Infraestrutura AWS com comando de Voz

<img src="https://media.giphy.com/media/HoffxyN8ghVuw/giphy.gif">

O Script funciona usando módulos de speech recognition, ou seja, é possivel executar comandos pré-programados com a voz,
* Diga: - Criar ec2
* Se tudo estiver ok receberá a confirmação por audio
<br>
O script irá chamar o módulo terraform que está dentro da pasta "terraform/", e criara uma ec2 simples, nada impede que você personalize com os próprios módulos e comandos de audio.
<br>
<br>

Para destruir a infraestrutura criada

* Diga: - Destruir Infraestrutura
* Se tudo estiver ok receberá a confirmação por audio

<br>

Atenção: é necessário criar diretório de nome "audios" na pasta raiz do script
