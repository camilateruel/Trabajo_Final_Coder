# Trabajo_Final_Coder
## Tema: Enfermedades del corazón

El dataset escogido para la presentación de este proyecto contiene datos de pacientes los cuales pueden tener o no predisposición a enfermdades cardíacas. Los datos fueron recolctados por la universidad "Donald Bren School of Information and Computer Sciences
University" en California. 
Este es un dataset de tipo multivariado lo cual significa que nos proveera con gran variedad de variables matemáticas que deberán ser analizadas.

# Objetivo del proyecto

*   Selección de un dataset al cual se pueda aplicar un analisis exhaustivo y aplicar modelos estadisticos para predecir en base a una variable target.
*   Realizar correcta lectura de los datos, incluyendo limpieza de datos y detectar  outliers.
*   Realizar analsis univariado, bivariado y multivariado del dataset
*   Determinar si el dataset cumple con los requistos para el desarrollo del proyecto final
*   Finalmente lograr responder las preguntas del problema principal planteado

# Descripción del Dataset

Segun la documentación, este dataset tiene 13 columnas:
<ol>
  <li>Edad: Edad de la persona en años</li>
  <li>Genero: 1=Masculino y 0=Femenino</li>
  <li>Tipo de dolor en el pecho: Exiten tres criterios para clasificar los distintos tipo de angina: 
  <ul>
    <li>Ubicación: el dolor en el pecho ocurre alrededor del esternón</li>
    <li>Causa: el dolor se experimenta después de la inducción de estrés emocional/físico</li>
    <li>Alivio: el dolor desaparece después de tomar nitroglicerina y / o descansar </li>
    </ul>

Este dataset contiene cuatro valores para la explicar del dolor en relacion con los puntos clasificadores anteriores
  <ul>
    <li>0: Angina típica (todos los criterios presentes)</li>
    <li>1: Angina atípica (se cumplen dos de los tres criterios)</li>
    <li>2: Dolor no anginoso (menos de un criterio satisfecho)</li>
    <li>3: Asintomático (no se cumple ninguno de los criterios) </li>
  </ul>
	<li>Presión arterial en reposo</li>
	<li>Colesterol sérico mg/dl</li>
	<li>Glucemia en ayunas > 120 mg/dl (probablemente diabético) 1 = verdadero; 0 = falso </li>
	<li>Resultados electrocardiográficos en reposo (valores=0,1,2)
    <ul>
    <li>0: normal</li>
    <li>1: tener una anomalía de la onda</li>
    <li>2: muestra hipertrofia ventricular izquierda probable o definitiva</li>
    </ul>
  </li>
	<li>Frecuencia cardíaca máxima</li>
	<li>Angina inducida por ejercicio (1 = si; 0 = no)</li>
	<li>Depresión inducida por el ejercicio en relación con el descanso</li>
	<li>La pendiente del segmento ST de ejercicio en su punto maximo( 0: descendente; 1: plano; 2: pendiente ascendente) </li>
	<li>Arterias con problemas</li>
	<li>Un trastorno sanguíneo llamado talasemia (0: NULO,1: defecto fijo,2: flujo sanguíneo normal,3: defecto reversible)</li>
 <li> Varible target: Enfermedad cardíaca (1 = no, 0 = sí)</li>
</ol>
