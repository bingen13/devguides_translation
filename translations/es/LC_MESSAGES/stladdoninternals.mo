��    7      �  I   �      �  �   �  �   W  �     �   �  8   �  b   �  �     O  �  %   
     .
  C   <
     �
  %   �
     �
     �
     �
  0   �
  \   ,  7   �  b   �  �   $  �   �  �   �  �     V   �  �   =  }   �  �   A  i   �  �   ?  ~   .  z   �  �  (  �   �  �  �  �  O  �   I     :  7   M  J  �  �   �  �  �  �   �  V     =   v  �   �  �  |   �   "  !  �"  �   �#  /   �$  B   %  C   F%  (   �%  �  �%  �   T'  �   2(  �   )  �   �)  7   �*  w   .+  �   �+  {  b,  6   �-     .  W   $.     |.  0   �.     �.      �.  0   �.  C    /  {   d/  @   �/  u   !0  �   �0  �   ,1  �   "2  �   �2  \   �3  �   �3  �   |4  �   5  �   �5  3  O6  �   �7  �   =8    �8  �   �:    �;  b  >    k@     oA  Z   �A  �  �A    ~C  6  �D  �   �F  Z   EG  F   �G     �G  m  �H  �   VJ  r  9K  H  �L  /   �M  B   %N  C   hN  (   �N     7      
                &         )   5                -   *           .          6             1   2   (   +       #              	   !   $          '                   4   /       ,            "   %                                                3   0        	* For system tray list: "shell_TrayWnd" (desktop object), "TrayNotifyWnd" (notification area), "SysPager" (system tray), "ToolbarWindow32" (first system tray icon). 	* Taskbar icons in Windows Vista/Server 2008 and later: Shell_TrayWnd" (Desktop), "RebarWindow32" (Taskbar), "MSTaskSwWClass" (Taskbar), "MSTaskListWClass") , (taskbar icon). 	*Taskbar icons in Windows XP/Server 2003: "Shell_TrayWnd" (Desktop), "RebarWindow32" (Taskbar), "MSTaskSwWClass" (Taskbar), "ToolbarWindow32"), (first taskbar icon). 	1. Each locator has a list of window paths (window class names) to be searched to locate the needed icons and their locations, and this list is used by another private function to obtain a list of icon names. 	1. NVDA will look up the location of the selected icon. 	2. NVDA will perform a series of mouse clicks (mouseEvents function, more on this routine below). 	2. The private function will use user32.dll's FindWindowEx to locate the handle to the icons list where the icons live (more on this in the next section). 	3. Once the handle is found, NVDA will locate the first icon via NVDAObjects.IAccessible.getNVDAObjectFromEvent function. Then NvDA will use object navigation emulation (object, does something, object = object.next) to locate the icons and store their names and location in a list, which will then be returned to the locator routines. # NVDA Add-on internals: SysTray List ## Conclusion ## FindWindow versus FindWindowEx and its relation to icon locators ## Introduction ## NVDA+F11: A behind the scenes tour ## References: ## Source code layout ## SysTray List add-on features ## The "magic" behind icon name locator function * An event executor (more on this below) that sends mouse events specified in the parameter. * Like any Python module, various modules are imported. * The dialog class (globalPlugins.systraylist.SystrayListDialog) for displaying the dialog itself. * The global plugin (class GlobalPlugin(globalPluginHandler.GlobalPlugin)) which contains the systray script and helper functions. 1. Determines if you pressed this command once or twice by calling scriptHandler.getLastScriptRepeatCount. If you press NvDA+F11 and then you press NVDA+F11 within the next half a second, NvDA will treat this as multiple press of this command. 1. FindWindow (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633499(v=vs.85).aspx 1. For element in the path to be searched, it calls FindWindowEx to locate the needed handle. At first, this handle is 0, and search begins from the shell (desktop) object (the root of all windows). 2. Depending on the icons you are looking for, NvDA will search the following windows: 2. FindWindowEx (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633500(v=vs.85).aspx 2. If NVDA sees that you have pressed NVDA+F11 once, NvDA will locate system tray icons, otherwise it'll fetch taskbar icons. 3. For each path (window handle if found), this function will ask Windows to search for the next window in the path and store the resulting handle. 3. The icon locators (both are private functions) will do the following to obtain a list of icons needed: 4. Once the locators obtain the list of icons and their locations, it'll call another private function to open a dialog and show the requested icons. Depending on script count, it'll change the title and the label for the icons list view. 5. After you select an icon and what to do (left click (default), right click, double-click), NVDA will perform the following: A big hint: you don't have to use this add-on to access list of system tray icons. To access system tray, press Windows+B. A hidden gem of this add-on is that there is no command to view taskbar icons (that command is taken by NVDA's review cursor selection copy command (NvDA+F10)). Instead, to view taskbar icons, press NVDA+F11 twice quickly (more on how this is possible in a second). The list view changes to show taskbar icons (including pinned items). Pressing ENTER will cause NVDA to perform a left mouse click. After installing this add-on, you can press NVDA+F11 to view a list of system tray icons. This dialog lists the icons in the notification area, as well as buttons to cilck, double-click and do right mouse clicks. Although the idea of listing system tray icons seems easy, there is a lot going on under the hood, involving locating the correct window via Windows API and carefully designing the user interface. This shows that designing a simple add-on like this involves careful thinking, especially if it'll be used by many users around the world. I hope this article was helpful in letting you understand how simple add-on suggestions are developed and designed. As more and more people are transitioning from JAWS for Windows to NVDA, a frequently asked question is whether NVDA has a dialog to show system tray (notification area) icons. By default, NVDA does not ship with such a feature, but it can be brought back with an add-on appropriately called "SysTray List". This add-on, developed by Rui Fontes and Rui Batista, allows you to view a list of system tray or taskbar icons, and this is the add-on we'll find out how it works in this add-on internals article. As opposed to FindWindow, FindWindowEx takes two additional parameters, namely the handle to a window where the search should begin and which child window to search (or a group of windows to search). This results in the following signature: Author: Joseph Lee For example, the above call to FindWindow could become: Important disclaimer: This add-on was not developed by the author of this article, and views expressed in this article are strictly the author's. SysTrayList add-on is copyright Rui Fontes and Rui Batista, Windows API is copyright Microsoft Corporation, NVDA is copyright NV Access, Python is copyright Python Software Foundation. In the original version, FindWindow would return a handle to a window given the class name and child window class name. For example, if we need to obtain a handle to a menu bar in an app, we would use: Lastly, I would like to stress the fact that JAWS for Windows and NonVisual Desktop Access are two completely different screen readers. Although they have borrowed features from each other, the underlying philosophy, license type (proprietary and commercial for JAWS versus open-source and GPL for NvDA), design and programming language in use are different. Thus, please do not expect all JAWS functionality suggestions to be investigated by NV Access, or Freedom Scientific to borrow every feature from NVDA. So what exactly happens when you press NVDA+F11? When you press this command after installing the add-on, NVDA will do the following: Specifying NULL (None) for the second parameter would search for the top-level window. The global plugin file is composed of the following sections: This global plugin lives in its own directory named sysTrayList (globalPlugins/sysTrayList/__init__.py). Some add-ons, especially those that use helper modules uses package-style directory structure. To download the add-on, go to https://addons.nvda-project.org/addons/systrayList.en.html, and for the source code, go to http://bitbucket.org/nvdaaddonteam/systraylist. Just like the previous series on StationPlaylist Studio, you don't have to use the add-on to learn about its internals, but having the source code and/or using the add-on could help you as you understand how this add-on works behind the scenes. When asked by NVDA, the icon name locator function (noted above) will try its best to locate the first system tray or taskbar icon. This is how it is done: When transitioning between screen readers, one of the first things people might ask is inclusion of familiar features from old screen reader in the new product. As a user who have worked with multiple screen readers, I often ask this question when moving from one screen reader to another. Windows API has changed a lot in more recent versions of Windows. This came as a response to security concerns, to extend API functionality and so on. Because of this, you may see many Windows API functions that ends with "Ex" (short for "extended"). hwnd = FindWindow("WindowClassName", "MenuBar") hwnd = FindWindowEx(handle, childGroup, className, childClassName) hwnd = FindWindowEx(parentHwnd, None, "WindowClassName", "MenuBar") parentHwnd = FindWindow("Desktop", None) Project-Id-Version: 
POT-Creation-Date: 2018-02-10 11:53+Hora estándar romance
PO-Revision-Date: 2018-02-21 13:12+0100
Last-Translator: José Manuel Delicado Alcolea <josemanuel.delicado@urjc.es>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.0.6
Plural-Forms: nplurals=2; plural=(n != 1);
 	* Para la lista de la bandeja del sistema: "shell_TrayWnd" (objeto del escritorio), "TrayNotifyWnd" (área de notificaciones), "SysPager" (bandeja del sistema), "ToolbarWindow32" (primer icono de la bandeja del sistema). 	* Iconos de la barra de tareas en Windows Vista / Server 2008 y posteriores: "Shell_TrayWnd" (Escritorio), "RebarWindow32" (Barra de tareas), "MSTaskSwWClass" (Barra de tareas), "MSTaskListWClass" (icono de la barra de tareas). 	* Para iconos en la barra de tareas en Windows XP / Server 2003: "Shell_TrayWnd" (Escritorio), "RebarWindow32" (Barra de tareas), "MSTaskSwWClass" (Barra de tareas), "ToolbarWindow32" (primer icono de la barra de tareas). 	1. Cada ubicador tiene una lista de rutas a ventanas (nombres de clase de ventanas) en las que buscar para encontrar los iconos necesarios y sus ubicaciones, esta lista se pasa a otra función privada para obtener una lista con los nombres de los iconos. 	1. NVDA buscará la ubicación del icono seleccionado. 	2. NVDA realizará una serie de clics con el ratón (función mouseEvents, más info sobre este procedimiento debajo). 	2. La función privada llamará a la función FindWindowEx de user32.dll para obtener el manejador de la lista de iconos donde estos se alojan (más sobre esto en la siguiente sección). 	3. Una vez se encuentra el manejador, NVDA ubicará el primer icono a través de la función NVDAObjects.IAccessible.getNVDAObjectFromEvent. A continuación, NVDA usará emulación de navegación por objetos (objeto, hace algo, objeto=objeto.next) para encontrar los iconos y almacenar sus nombres y posiciones en una lista, que será devuelta a los procedimientos del ubicador. # Complementos de NVDA vistos por dentro: SysTray List ## Conclusión ## Diferencias entre FindWindow y FindWindowEx y relación con los ubicadores de iconos ## Introducción ## NVDA+f11: recorrido por detrás del escenario ## Referencias: ## Estructura del código fuente ## Características del complemento SysTray List ## La "magia" detrás de la función buscadora de nombres de iconos * Un ejecutor de eventos (más información sobre esto debajo) que envía los eventos de ratón que recibe como parámetro. * Como en cualquier módulo Python, se importan varios módulos. * La clase del diálogo (globalPlugins.systraylist.SystrayListDialog), encargada de mostrar el diálogo en cuestión. * La extensión global (class GlobalPlugin(globalPluginHandler.GlobalPlugin)), que contiene el script de bandeja del sistema y funciones auxiliares. 1. Determina si has pulsado esta orden una o dos veces llamando a scriptHandler.getLastScriptRepeatCount. Si pulsas NVDA+f11 y lo vuelves a pulsar en el siguiente medio segundo, NVDA tratará este hecho como múltiples pulsaciones de esta orden. 1. Referencia de FindWindow (user32.dll) (Api de Windows): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633499(v=vs.85).aspx 1. Para cada elemento en la ruta de búsqueda, se llama a FindWindowEx para obtener su manejador. Al principio, este manejador es 0, y la búsqueda comienza desde la raíz de todas las ventanas, el objeto escritorio de la Shell. 2. Dependiendo de los iconos que hayas solicitado, NVDA buscará en las siguientes ventanas: 2. Referencia de FindWindowEx (user32.dll) (Api de Windows): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633500(v=vs.85).aspx 2. Si NVDA ve que has pulsado NVDA+f11 una vez, localizará los iconos de la bandeja del sistema, en caso contrario recopilará los iconos de la barra de tareas. 3. Para cada ruta (manejador de ventana si se encuentra), esta función pedirá a Windows que busque la próxima ventana en la ruta y almacenará el manejador correspondiente. 3. Los ubicadores de iconos (ambos son funciones privadas) harán lo siguiente para obtener una lista con los iconos necesarios: 4. Una vez los ubicadores hayan obtenido las listas de iconos y sus posiciones, se llama a otra función privada para abrir un diálogo y mostrar los iconos solicitados. Dependiendo del número de veces que se ha pulsado la orden, el script cambiará el título y la etiqueta de la vista de lista de iconos. 5. Después de seleccionar un icono e indicar lo que quieres hacer con él (clic con el botón izquierdo (por defecto), clic con el botón derecho, doble clic), NVDA hará lo siguiente: Sugerencia importante: no tienes que usar este complemento para listar los iconos de la bandeja del sistema. Para acceder a la bandeja del sistema, pulsa Windows+B. Una joya oculta de este complemento es que no hay una orden para ver los iconos de la barra de tareas (esta orden se asigna a la opción de copiar texto al portapapeles seleccionado por el cursor de revisión (NVDA+f10)). En su lugar, para ver los iconos de la barra de tareas, pulsa NVDA+f11 dos veces rápidamente (en un segundo se puede pulsar incluso más veces). La vista de lista cambia para mostrar los iconos de la barra de tareas (incluyendo elementos anclados). Al pulsar intro NVDA simula un clic con el botón izquierdo. Tras instalar este complemento, puedes pulsar NVDA+f11 para ver la lista de iconos de la bandeja del sistema. Este diálogo lista los iconos del área de notificaciones, y tiene botones para hacer clic, doble clic y clic con el botón derecho del ratón. Aunque la idea de listar iconos de la bandeja del sistema parece fácil, hay mucho trabajo de fondo, que implica ubicar la ventana correcta a través de la Api de Windows y diseñar la interfaz de usuario cuidadosamente. Esto muestra que diseñar un complemento simple como este implica pensar cuidadosamente, especialmente sabiendo que será usado por muchos usuarios de todo el mundo. Espero que este artículo haya sido útil a la hora de hacerte entender cómo se desarrolla y diseña una sugerencia de un complemento simple. Cuanta más y más gente hace la transición desde Jaws for Windows a NVDA, más surge con frecuencia la pregunta de si NVDA dispone de un diálogo para mostrar los iconos de la bandeja del sistema (también llamada área de notificaciones). Por defecto, NVDA no incluye esta característica de serie, pero podemos tenerla de vuelta gracias a un complemento llamado apropiadamente "SysTray List". Este complemento, desarrollado por Rui Fontes y Rui Batista, permite ver una lista con los iconos de la bandeja del sistema o la barra de tareas, y este es el complemento que veremos con detalle en este artículo. Al contrario que en FindWindow, FindWindowEx recibe dos parámetros adicionales, uno es el manejador de la ventana donde debería comenzar la búsqueda y el otro en qué ventana hija buscar (o en qué grupo de ventanas hijas). Esto se traduce en lo siguiente: Autor: Joseph Lee Por ejemplo, la llamada de más arriba a FindWindow podría quedar de la siguiente manera: Descargo de responsabilidad: este complemento no ha sido desarrollado por el autor de este artículo, y los puntos de vista expresados en este artículo son estrictamente del autor del mismo. El complemento SysTray List tiene copyright de Rui Fontes y Rui Batista, la api de Windows tiene copyright de Microsoft Corporation, NVDA tiene copyright de NV Access y Python tiene copyright de la Python Software Foundation. En la versión original, FindWindow devolvería un manejador a una ventana pasándole el nombre de clase de esta ventana y el nombre de clase de la ventana hija. Por ejemplo, si queremos obtener el manejador para una barra de menú en una aplicación, usaríamos: Finalmente, me gustaría resaltar el hecho de que Jaws for Windows y Non Visual Desktop Access son dos lectores de pantalla completamente diferentes. Aunque ambos han tomado prestadas funciones del otro, la filosofía de fondo, tipo de licencia (propietaria y comercial para Jaws contra GPL y de código abierto para NVDA), diseño y lenguaje de programación utilizado son diferentes. Por lo tanto, no esperes que todas las sugerencias de características de Jaws sean investigadas por NV Access, o que Freedom Scientific tome prestada cada característica de NVDA. ¿Qué ocurre exactamente cuando pulsas NVDA+f11? Cuando pulsas esta orden después de instalar el complemento, NVDA hace lo siguiente: Si se pasa NULL (None) como segundo parámetro se buscaría la ventana de más alto nivel. El fichero de extensión global se divide en las siguientes secciones: Esta extensión global reside en su propia carpeta, llamada sysTrayList (globalPlugins/sysTrayList/__init__.py). Algunos complementos, especialmente aquellos que se apoyan en módulos auxiliares, siguen un estilo de paquete en su estructura de directorios. Para descargar el complemento, visita la sección correspondiente en el menú principal de esta página, y para acceder al código fuente, visita http://bitbucket.org/nvdaaddonteam/systraylist. No es necesario que uses este complemento para conocer cómo está hecho por dentro, pero tener su código fuente y/o usarlo puede ayudarte a conocer mejor cómo funciona. Cuando NVDA la llama, la función buscadora de nombres de iconos (de la que hemos hablado arriba) dará lo mejor de sí misma para encontrar el primer icono de la bandeja del sistema o la barra de tareas. Así es como lo hace: Al hacer la transición entre lectores de pantalla, una de las primeras cosas que alguien podría preguntarse es si existen características del antiguo lector de pantalla en el nuevo a las que la gente ya esté acostumbrada. Como usuario que ha trabajado con varios lectores de pantalla, frecuentemente me hago esta pregunta cuando paso de un lector de pantalla a otro. La api de Windows ha cambiado muchísimo en versiones recientes de este sistema operativo. Estos cambios se dieron como una reacción ante problemas de seguridad, para extender la funcionalidad de la api, etc. Por este motivo, pueden verse muchas funciones de la api de Windows que terminan con "Ex" (abreviatura de "extended"). hwnd = FindWindow("WindowClassName", "MenuBar") hwnd = FindWindowEx(handle, childGroup, className, childClassName) hwnd = FindWindowEx(parentHwnd, None, "WindowClassName", "MenuBar") parentHwnd = FindWindow("Desktop", None) 