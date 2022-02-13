#!/usr/bin/env python
# coding: utf-8

# # TRABAJO FINAL CODERHOUSE

# ## Enfermedades del corazón
# 
# El dataset escogido para la presentación de este proyecto contiene datos de pacientes los cuales pueden tener o no predisposición a enfermdades cardíacas. Los datos fueron recolctados por la universidad "Donald Bren School of Information and Computer Sciences University" en California. 
# 
# Este es un dataset de tipo multivariado lo cual significa que nos proveera con gran variedad de variables matemáticas que deberán ser analizadas. 
# 
# Para fines de hacerlo más real a los planteos del trabajo, se trabajará con la premisa de que los integrantes del grupo somos miembros del área de investigación del "Hospital Nacional Universitario CoderHouse".

# # Contenido
# 1. [Equipo de trabajo](#1)
# 2. [Objetivos](#2)
# 3. [Criterios de selección del Dataset](#3)
# 4. [Descripción del Dataset](#4)

# # 1.Equipo de trabajo <a name="1"></a>
# 
# 
# Este proyecto sera desarrollado por dos estudiantes del curso Data Science en [CoderHouse.](https://www.coderhouse.com) 
# 
# 
# 1.   Camila Teurel
# 2.   Carlos Medina
# 
# 

# ## 2. Objetivo del proyecto <a name="2"></a>
# 
# *   Selección de un dataset al cual se pueda aplicar un analisis exhaustivo y aplicar modelos estadisticos para predecir en base a una variable target.
# *   Realizar correcta lectura de los datos, incluyendo limpieza de datos y detectar  outliers.
# *   Realizar analsis univariado, bivariado y multivariado del dataset
# *   Determinar si el dataset cumple con los requistos para el desarrollo del proyecto final
# *   Finalmente lograr responder las preguntas del problema principal planteado

# ## 3.Criterios de selección del Datase <a name="3"></a>
# 
# Decidimos avanzar con el dataset de enfermedades cardíacas, ya que contamos con la información suficiente para poder predecir en base a las variables patrones comunes en pacientes que sufren de enfermedades cardíacas y de ser posible encontrar condiciones óptimas para disminuir las probabilidades de enfermedades cardíacas.
# 
# Adicionalmente el criterio de decisión del dataset se respalda más adelante con los analisis univariado de las variables, analisis bivariados respecto a la variable target, perfilado de las variables donde se observan que tipo de distribuciones siguen las mismas y así poder detectar valores atípicos que pueden modificar los resultados del estudio.
# 

# ## 4.Descripción del Dataset <a name="4"></a>
# 
# Segun la documentación, este dataset tiene 13 columnas:
# <ol>
#   <li>Edad: Edad de la persona en años</li>
#   <li>Genero: 1=Masculino y 0=Femenino</li>
#   <li>Tipo de dolor en el pecho: Exiten tres criterios para clasificar los distintos tipo de angina: 
#   <ul>
#     <li>Ubicación: el dolor en el pecho ocurre alrededor del esternón</li>
#     <li>Causa: el dolor se experimenta después de la inducción de estrés emocional/físico</li>
#     <li>Alivio: el dolor desaparece después de tomar nitroglicerina y / o descansar </li>
#     </ul>
# 
# Este dataset contiene cuatro valores para la explicar del dolor en relacion con los puntos clasificadores anteriores
#   <ul>
#     <li>0: Angina típica (todos los criterios presentes)</li>
#     <li>1: Angina atípica (se cumplen dos de los tres criterios)</li>
#     <li>2: Dolor no anginoso (menos de un criterio satisfecho)</li>
#     <li>3: Asintomático (no se cumple ninguno de los criterios) </li>
#   </ul>
# 	<li>Presión arterial en reposo</li>
# 	<li>Colesterol sérico mg/dl</li>
# 	<li>Glucemia en ayunas > 120 mg/dl (probablemente diabético) 1 = verdadero; 0 = falso </li>
# 	<li>Resultados electrocardiográficos en reposo (valores=0,1,2)
#     <ul>
#     <li>0: normal</li>
#     <li>1: tener una anomalía de la onda</li>
#     <li>2: muestra hipertrofia ventricular izquierda probable o definitiva</li>
#     </ul>
#   </li>
# 	<li>Frecuencia cardíaca máxima</li>
# 	<li>Angina inducida por ejercicio (1 = si; 0 = no)</li>
# 	<li>Depresión inducida por el ejercicio en relación con el descanso</li>
# 	<li>La pendiente del segmento ST de ejercicio en su punto maximo( 0: descendente; 1: plano; 2: pendiente ascendente) </li>
# 	<li>Arterias con problemas</li>
# 	<li>Un trastorno sanguíneo llamado talasemia (0: NULO,1: defecto fijo,2: flujo sanguíneo normal,3: defecto reversible)</li>
#  <li> Varible target: Enfermedad cardíaca (1 = no, 0 = sí)</li>
# </ol>

# En otra notebook presentaremos el desarrollo del trabajo realizado.
