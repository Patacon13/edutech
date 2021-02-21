# Edutech

## Primera versión de detección de voz

Se utilizó el software de Snowboy para la detección de palabras (en principio, la palabra "Dos") grabado desde una Raspberry Pi y compilado en Ubuntu 20.04

### Instrucciones originales:

-Clonar repo-

git clone https://github.com/Patacon13/edutech/
cd edutech

-Instalar-
Generar virtual environment
virtualenv -p python2 venv/snowboy

-Ingresar-
source venv/snowboy/bin/activate

-Instalar portaudio-
sudo apt install portaudio19-dev python3-pyaudio

-Instalar sox-
sudo apt-get install sox

-Trabajar en Python-
cd examples
cd Python

-Instalar dependencias-
pip2 install -r requirements.txt
Necesario: 3 wav files en 16000 sample rate, 16 bits, 1 channel
rec -r 16000 -c 1 -b 16 -e signed-integer -t wav record1.wav

-Entrenar modelo-
Modificar antes en /pmdl snowboy_pmdl para permitir compatibilidad
python2 generate_pmdl.py -r1=record1.wav -r2=record2.wav -r3=record3.wav -lang=en -n=hotword.pmdl

-Instalar swig-
wget http://downloads.sourceforge.net/swig/swig-3.0.10.tar.gz

-Descomprimir swig-
sudo apt-get install libpcre3 libpcre3-dev
./configure --prefix=/usr --without-clisp --without-maximum-compile-warnings
make
make install

-Compilar detector-
cd /swig/Python
Make

-Instalar atlas-
sudo apt-get install libatlas-base-dev

Para probar una demo del modelo creado
cd /examples/Python
python2 demo.py hotword.pmdl
