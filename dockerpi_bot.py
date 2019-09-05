#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import os

TOKEN = ""  # SUSTITUIR POR TU TOKEN
ID = # SUSTITUIR PO TU ID NO PONER COMILLAS

userStep = {}
knownUsers = []

commands = {
        'ayuda': 'Comandos disponibles',
        'start': 'Arranca el bot',
    'images': 'Mostrar imagenes',
    'image_remove': 'Elimina la imagen que le haya especificado',
    'containers_active': 'Muestra contenedores activos',
    'containers_inactive': 'Muestra contenedores inactivos',
        'container_create': 'Crea el contenedor con la imagen que le haya especificado',
        'container_start': 'Activa el contenedor que le haya especificado',
    'container_stop': 'Inactiva el contenedor que le haya especificado',
    'container_remove': 'Elimina el contenedor que le haya especificado',
    'search': 'Busca las imagenes que le haya especificado',
    'pull': 'Descargar la imagen que le haya especificado',
    'logs': 'Muestra los logs del contenedor que le haya especificado',
    'version': 'Muestra la version de Docker',
}


# USER STEP
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0

# LISTENER
def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print("[" + str(m.chat.id) + "] " + str(m.chat.first_name) + ": " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)


# START
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid == ID :
      userStep[cid] = 0
      time.sleep(1)
      bot.send_message(cid, "Pulsa /ayuda para ver los comandos disponibles\n")
    else:
        bot.send_message(cid, " ¡¡NO ERES MI CREADOR!!")

# AYUDA
@bot.message_handler(commands=['ayuda'])
def command_ayuda(m):
    cid = m.chat.id
    if cid == ID :

      #help_text = "Comandos disponibles: \n"
      #for key in commands:
      #  help_text += "/" + key + ": "
      #  help_text += commands[key] + "\n"
      bot.send_message(cid, "/ayuda muestra los comandos disponibles\n"
          "/images Mostrar imagenes\n"
          "/image_remove Elimina la imagen que le haya especificado\n"
      "/containers_active Muestra contenedores activos\n"
          "/containers_inactive Muestra contenedores inactivos\n"
          "/container_create Crea el contenedor con la imagen que le haya especificado \n"
          "/container_start Activa el contenedor que le haya especificado\n"
          "/container_stop Inactiva el contenedor que le haya especificado\n"
      "/container_remove Elimina el contenedor que le haya especificado\n"
      "/search Busca las imagenes que le haya especificado\n"
      "/pull Descargar la imagen que le haya especificado\n"
      "/logs Muestra los logs del contenedor que le haya especificado\n"
      "/version Muestra la version de Docker\n")
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")

# COMANDO images
@bot.message_handler(commands=['images'])
def command_images(m):
    cid = m.chat.id
    if cid == ID :
      images = os.popen('sudo docker images')
      result = images.read()
      bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO image_remove
@bot.message_handler(commands=['image_remove'])
def command_image_remove(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Eliminando: " + m.text[len("/image_remove"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker rmi' + m.text[len("/image_remove"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO containers_active
@bot.message_handler(commands=['containers_active'])
def command_images(m):
    cid = m.chat.id
    if cid == ID :
      containers_active = os.popen('sudo docker ps')
      result = containers_active.read()
      bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO containers_inactive
@bot.message_handler(commands=['containers_inactive'])
def command_images(m):
    cid = m.chat.id
    if cid == ID :
      containers_inactive = os.popen('sudo docker ps -a')
      result = containers_inactive.read()
      bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO container_create
@bot.message_handler(commands=['container_create'])
def command_container_create(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Creando contenedor: " + m.text[len("/container_start"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker create' + m.text[len("/container_create"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO container_start
@bot.message_handler(commands=['container_start'])
def command_container_start(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Iniciando contenedor: " + m.text[len("/container_start"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker start' + m.text[len("/container_start"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO container_stop
@bot.message_handler(commands=['container_stop'])
def command_container_stop(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Apagando contenedor: " + m.text[len("/container_stop"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker stop' + m.text[len("/container_stop"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO container_remove
@bot.message_handler(commands=['container_remove'])
def command_container_remove(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Eliminando contenedor: " + m.text[len("/container_remove"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker rm' + m.text[len("/container_remove"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO search
@bot.message_handler(commands=['search'])
def command_search(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Buscando imagen: " + m.text[len("/search"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker search' + m.text[len("/search"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO pull
@bot.message_handler(commands=['pull'])
def command_search(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Buscando imagen: " + m.text[len("/pull"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker pull' + m.text[len("/pull"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO logs
@bot.message_handler(commands=['logs'])
def command_logs(m):
    cid = m.chat.id
    if cid == ID :
        bot.send_message(cid, "Logs del contenedor: " + m.text[len("/logs"):])
        bot.send_chat_action(cid, 'typing')
        time.sleep(4)
        f = os.popen('sudo docker logs' + m.text[len("/logs"):])
        result = f.read()
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# COMANDO version
@bot.message_handler(commands=['version'])
def command_version(m):
    cid = m.chat.id
    if cid == ID :
      version = os.popen('sudo docker version')
      result = version.read()
      bot.send_message(cid, result)
    else:
        bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
        print(color.RED + " ¡¡PERMISO DENEGADO!! " + color.ENDC)

# FILTRAR MENSAJES
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_text(m):
    cid = m.chat.id
    if (m.text.lower() in ['hola', 'hi', 'buenas', 'buenos dias', 'oli']):
        bot.send_message(cid, 'Muy buenas, ' + str(m.from_user.first_name) + '. Me alegra verte de nuevo.')
    elif (m.text.lower() in ['adios', 'aios', 'adeu', 'ciao', 'dew']):
        bot.send_message(cid, 'Hasta luego, ' + str(m.from_user.first_name) + '. Te echaré de menos.')

print 'Corriendo...'
bot.polling(none_stop=True)
