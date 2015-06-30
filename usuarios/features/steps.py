# -*- coding: utf-8 -*-
from lettuce import *
from lettuce.django import django_url
from nose.tools import assert_equals
from splinter.browser import Browser
#from usuarios.models import Usuario


@step(u'voy a la direccion "(.*)" url')
def la_direccion_url(step,url):
    world.browser.get(url)


@step(u'Then deberia ver "(.*)"')
def then_deberia_ver_content(step,content):
    world.browser.implicitly_wait(4)
    if content not in world.browser.find_element_by_id("content").text:
        raise Exception("Pagina no encontrada.")

# @step(u'un usuario se quiere registrar "(.*)"')
# def un_usuario_se_quiere_registrar(step,nombre):
#     Usuario=Usuario(nombre=nombre)
#     Usuario.save()
#
# @step(u'El llena el "(.*)" con "(.*)"')
# def el_llena_el(step,field,value):
#     world.browser.fill(field,value)
#
# @step(u'El presiona "(.*)"')
# def el_presiona(step,button_label):
#     button=world.browser.find_element_byid('//button[text()="%s"]') % button_label.first
#
# @step(u'El deberia ver "(.*)"')
# def el_deberia_ver(step,text):
#     assert text in world.browser.html
#
# @step(u'El usuario existente es "(.*)"')
# def el_usuario_existente_es(step,campo):
#     Usuario=Usuario(pseudonimo=campo,email=campo)
#     Usuario.save()
