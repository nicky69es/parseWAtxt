parseWAtxt
Create a report with the contents of WhatsApp conversations extracted in .txt files

Este programa crea un informe con el contenido de los archivos "txt" que crea la extracción de las conversaciones en Whatsapp. Busca los archivos de conversaciones dentro de un directorio, calcula su hash sha256 e incluye en el informe

Cada uno puede adaptarlo a sus necesidades incluyendo librerías de docx o pdf para obtener un informe con mejor presentación que pueda incluir las imágenes adjuntas en las conversaciones.

Está realizado para utf-8, por lo que puede dar problemas con otras codificaciones de texto.

PROCESO PARA EXTRAER LAS CONVERSACIONES DE WA CUANDO UNA HERRAMIENTA FORENSE NO PUEDE.

METODO 1 (Testado en Galaxy S9+ con Android 8.0.0 y parche de seguridad de nov18)

Con el terminal encendido: Paso 1: Abrir whatsapp e ir a "Ajustes > Chats > Historial de Chats" Paso 2: "Exportar chat" Paso 3: Seleccionar una conversación activa. Paso 4: En caso de que nos pregunte sobre incluir archivos multimedia, responder según interés. Paso 5: Al salir el modo de exportación (BT, Mail, etc), NO SELECCIONAR NINGUNO!. Paso 6: Volver al paso 2 y seleecionar la siguiente conversación en el paso 3, hasta hacerlo con todas las conversaciones que nos interese extraer. SOLO CUANDO HAYAMOS FINALIZADO DE EXPORTAR CONVERSACIONES Paso 7: Conectar cable OTG y pendrive USB al terminal. Paso 8: A través del navegador de archivos del propio terminal, copiar la carpeta "WhatsAPP" y pegarla en nuestro USB.

La carpeta que hemos copiado contiene 4 carpetas:

".Shared" que contiene los txt y zip de las conversaciones que hemos pedido exportar. (Es un archivo temporal que se crear para el envío por alguno de los sistemas que propone en el paso 5).
".trash" desconozco al encontrarla sin contenido.
"Databases" contiene una copia de la msgstore.db.crypt. Sin key.
"Media" contiene los archivos multimedia separados en carpetas por tipo, así como Wallpapers y Statuses
METODO 2 (Testado en BQ Aquaris M5 y Android 7)

Con el terminal encendido: Paso 1: Abrir whatsapp e ir a "Ajustes > Chats > Historial de Chats" Paso 2: "Exportar chat" Paso 3: Seleccionar una conversación activa. Paso 4: En caso de que nos pregunte sobre incluir archivos multimedia, responder según interés. Paso 5: Al salir el modo de exportación (BT, Mail, etc), seleccionar GMail. Paso 6: Se generará un email que llevará como fichero adjunto el txt del chat exportado.

RECOMENDACIONES: Crear un .zip con la carpeta extraída y calcular hash. Duplicar el zip y comprobar hash. Trabajar con este script en la carpeta copiada y guardar los zip como evidencias.

Pretendo mejorar: Leer los archivos txt de el zip creado.

Está abierto a mejoras. Preferiria que las mejoras fueran sin necesidad de modulos que sea necesario instalar en el equipo.

Mejoras de última versión: Ya le puedes pasar como parámetro al script el directorio donde se encuentran los txt, y generará el informe allí. Si no pasas ningún parámetro trabaja en el directorio actual.

Ejemplo de uso: python parseWAtxt.py directorio_de_los_txt

# parseWAtxtToScreen
Create a report with the contents of WhatsApp conversations extracted in .txt files to Screen

Ejemplo de uso: python parseWAtxtToScreen.py directorio_de_los_txt

Para obtener el informe en un fichero redirigir.

Ejemplo de uso: python parseWAtxtToScreen.py directorio_de_los_txt ruta/nombre_fichero_informe.txt
