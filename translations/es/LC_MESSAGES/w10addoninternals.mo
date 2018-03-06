��    ,      |  ;   �      �  2   �     �          )  (   9     b     p  �   �  y   6  R  �  �     x   �  g   o    �  y   �	  w   d
  p   �
  {   M  �   �  Q  J  �   �  B   0  C   s  z   �  l   2  F  �  N   �  .   5     d  �   w  �   I  �  �  [  �     7  �  O  -     n   N  �  �  <  R   0   �!  A   �!  [  "  k  ^$  �  �%  C   k'     �'     �'     �'  +   �'     )(     8(  �   M(  �   )  �  �)  ;  I+  z   �,  n    -  o  o-  �   �.  �   e/  w   �/  �   d0  ~   �0  �  n1  �   �2  B   �3  C   �3  �   ;4  l   �4  �  +5  n   �6  N   7     n7  �   �7  �   o8  �  "9  |  �<     1>  u  N>  �  �A  �   �D  W  <E  l  �I  0   K  O   2K  �  �K  �  hN        
         *   #                       ,      $       "   %          	         '   &                                     (   !                                         )          +                        # NVDA Add-on internals: Windows 10 App Essentials ## Add-on contents ## Introducing Windows 10 ## Introduction ## Purposes of Windows 10 App Essentials ## References ### Startup and shutdown * Auto-suggest accessibility, part of Accessible Text Requirements (Microsoft Docs): https://docs.microsoft.com/en-us/windows/uwp/accessibility/accessible-text-requirements * Component Object Model Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ms680573(v=vs.85).aspx * Demonstrating commitment to accessibility advocacy: some accessibility champions, including I, have recently stressed that accessibility is important in app designs, and that developers should take accessibility feedback seriously. Through workarounds and features, the add-on provides a way to demonstrate this commitment and advocacy. * Essential features and announcements: Until early 2017, NVDA did not announce important information such as status of Windows Update installations in Settings app. This is about to change (see notes on live region change event for details). * IUIAutomationElement interface (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671425(v=vs.85).aspx * MSAA overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/dd373592(v=vs.85).aspx * New features support: part of making sure screen reader users were treated with respect was showcasing new Windows 10 features early through this NVDA add-on. These include support for really old versions of Feedback Hub app, emoji panel in Fall Creators Update and so on. * UI Automation Event Identifiers (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671223(v=vs.85).aspx * UI Automation Events Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671221(v=vs.85).aspx * UI Automation Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee684076(v=vs.85).aspx * UI Automation Properties Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671594(v=vs.85).aspx * UI Automation and Active Accessibility (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671585(v=vs.85).aspx * UI Automation and accessibility workarounds: every day, new features and bug fixes are added to various universal apps or Windows 10 itself. At the same time, there is at least one app where accessibility, particularly UI Automation, gets broken. Some of the add-on code is devoted to providing workarounds for odd UIA implementations. * What's a Universal Windows Platform (UWP) App (Microsoft UWP App Developer): https://docs.microsoft.com/en-us/windows/uwp/get-started/whats-a-uwp * Windows 10 (Wikipedia): https://en.wikipedia.org/wiki/Windows_10 * Windows Insider Program (Microsoft): https://insider.windows.com/ * Windows as a Service Overview (Microsoft Docs): https://docs.microsoft.com/en-us/windows/deployment/update/waas-overview * cachedAutomationId (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671434(v=vs.85).aspx 1. Enables tracking of missing UIA events. For example, until May 2017, controller for event (an event fired by a control that depends on another control such as an edit field with search suggestions) wasn't available in NVDA screen reader, but search suggestion announcement was made possible as this add-on added this event. 2. Adds user interface elements for this add-on, specifically add-on settings. 3. Checks for add-on updates if told to do so. Author: Joseph Lee Copyright: Microsoft Windows, Windows 10, Windows API, UI Automation, Microsoft Edge, Universal Windows Platform (UWP) and related technologies are copyright Microsoft Corporation. NVDA is copyright NV Access. Disclaimer: Despite the article text and knowledge that's contained within, I (Joseph Lee, the add-on author) do not work for NV Access nor Microsoft. I call the October 2014 preview (build 9841) a maiden flight for several reasons. First, this is the first time where Microsoft did show interest in user-level feedback. Although betas existed for earlier versions such as Windows 7 and 8.1, Windows 10 is the first attempt from Microsoft at connecting with users and taking comments seriously. Second, build 9841 (the first Insider Preview build) hailed the start of Windows as a Service, a completely different approach to upgrading Windows where Microsoft wanted to provide two things: continuous delivery and feedback loop, and a unified configuration that works well with most devices. There were setbacks, such as privacy concerns due to telemetry, but for the most part, Windows 10 was received positively. In NVDA Add-on Internals: Windows 10 App Essentials, we'll look at how this add-on came about, how it works, and go over recommendations from the add-on author (me) regarding accessibility practices. You'll also glimpse how UI Automation works at a high level, how features start out as an add-on component and end up as an NVDA feature and so on. Revision: December 2017 Supporting new technologies can be fun and challenging, especially a new operating system version that changes how people perform certain tasks and introduces new ways of keeping up with changes. This is more so when it comes to letting screen readers support new operating systems such as Windows 10, which brings new ways of interacting with a computer, new set of apps and technologies, and accessibility improvements and challenges. NVDA includes solid support for Windows 10, including Microsoft Edge, the new Start menu, navigation in universal apps and so on, all made possible thanks to collaboration between users, Microsoft, NV Access and others, part of which involves the add-on we will meet in this article. The Windows 10 App Essentials add-on consists of a global plugin and app modules for various universal apps that comes with Windows 10. The Windows 10 Objects (shortened to WinTenObjs), the global plugin portion of this add-on, provides foundations such as overlay classes for frequently encountered controls in Windows 10 an universal apps, UIA event tracking and logger, as well as the add-on update facility. Details of how the add-on updater works is covered in the article on StationPlaylist Studio add-on, as both add-ons use the same update facility. The only thing done at shutdown is terminating the update check facility and removing user interface elements. There is another, more personal reason for calling October 2014 release a maiden flight: I became one of the first Windows Insiders, and due to my work on NVDA, I have decided to make sure screen reader users were treated with respect. This included sending accessibility-related feedback, getting other screen reader users onboard as Insiders, and releasing NVDA try builds that resolved important issues for Windows Insiders. This culminated in the release of Windows 10 App Essentials add-on in November 2015 (in time for Windows 10 Version 1511/build 10586 release) that provided basic support for Insider Hub (now Feedback Hub) and other workarounds, which translated to superb user experience for NVDA users when it comes to using Windows 10 and various universal apps. My work on championing accessibility continues today, especially when it comes to making sure third-party universal apps are usable by many. To download the add-on, visit https://addons.nvda-project.org/addons/wintenApps.en.html. The source code for this add-on can be found at https://github.com/josephsl/wintenApps. As Windows 10 and universal apps are UI Automation universes, it is essential that you know some things about UIA, which are covered later. When the add-on loads, it performs three things: Windows 10 App Essentials add-on is built on top of four pillars: Windows 10 is the "last major" version of Windows for the foreseeable future. It introduces a completely new way of keeping track of changes through Windows Insider Program and Windows as a Service (WaaS, a fancy term for continuous delivery), new application development framework, unification strategy in terms of user experience across devices and a new web browser. In addition, it features the return of an older style of Start menu, virtual desktops, Action Center to centralize notifications, a way to run command-line Linux utilities, and revamped Narrator that continues to receive refinements. Windows 10 made its maiden flight in October 2014. Back then, it was called Windows Technical Preview, and after several weeks, it was renamed to Windows Insider Program. Between October 2014 and July 2015 when Windows 10 Version 1507 (build 10240) shipped, more than five million users became Insiders, testing new builds and apps, submitting feedback and so on. Project-Id-Version: 
POT-Creation-Date: 2018-02-10 11:53+Hora estándar romance
PO-Revision-Date: 2018-03-06 17:52+0100
Last-Translator: José Manuel Delicado Alcolea <josemanuel.delicado@urjc.es>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.0.6
Plural-Forms: nplurals=2; plural=(n != 1);
 # Complementos de NVDA vistos por dentro: Windows 10 App Essentials ## Contenidos del complemento ## Presentación de Windows 10 ## Introducción ## Propósitos de Windows 10 App Essentials ## Referencias ### Inicio y apagado * Accesibilidad de sugerencias automáticas, parte de los requisitos de textos accesibles (Microsoft Docs): https://docs.microsoft.com/en-us/windows/uwp/accessibility/accessible-text-requirements * Descripción de Component Object Model (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ms680573(v=vs.85).aspx * Demostración de compromiso y promoción de la accesibilidad: algunos defensores de la accesibilidad, incluyéndome a mí, hemos subrayado recientemente que la accesibilidad es importante en los diseños de aplicaciones, y que los desarrolladores deberían tomarse los comentarios de accesibilidad en serio. A través de características y solución de errores, el complemento ofrece una forma de demostrar este compromiso y promoción. * Características esenciales y verbalización: hasta principios del 2017, NVDA no verbalizaba información importante, como el estado de la instalación de actualizaciones en la aplicación de configuración. Esto está a punto de cambiar (mira las notas del evento de cambio en región activa para más detalles). * La interfaz IUIAutomationElement (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671425(v=vs.85).aspx * Descripción de MSAA (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/dd373592(v=vs.85).aspx * Soporte de nuevas características: una forma de asegurarse de que los usuarios de lectores de pantalla eran tratados con respeto era adaptando características de Windows 10 según aparecían a través de este complemento. Entre ellas se incluyen un soporte para la antigua aplicación del centro de comentarios, y el panel de emojis en Windows 10 creators update. * Identificadores de eventos en UI Automation (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671223(v=vs.85).aspx * Descripción de los eventos de UI Automation (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671221(v=vs.85).aspx * Descripción de UI Automation (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee684076(v=vs.85).aspx * Descripción de las propiedades de UI Automation (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671594(v=vs.85).aspx * UI Automation y Active Accessibility (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671585(v=vs.85).aspx * Solución de problemas de accesibilidad y UI Automation: cada día se añaden nuevas funciones y se solucionan fallos en diversas aplicaciones universales y en el propio Windows 10. Al mismo tiempo, hay al menos una aplicación donde la accesibilidad, particularmente la de UI Automation, se rompe. Parte del código del complemento se destina a solucionar implementaciones defectuosas de UIA. * Qué es una aplicación de la plataforma de Windows universal (UWP) (desarrollador de aplicaciones Microsoft UWP): https://docs.microsoft.com/en-us/windows/uwp/get-started/whats-a-uwp * Windows 10 (Wikipedia): https://en.wikipedia.org/wiki/Windows_10 * Windows Insider Program (Microsoft): https://insider.windows.com/ * Descripción de Windows como servicio (Microsoft Docs): https://docs.microsoft.com/en-us/windows/deployment/update/waas-overview * cachedAutomationId (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671434(v=vs.85).aspx 1. Activa el rastreo de eventos UIA ausentes. Por ejemplo, hasta mayo de 2017, el controlador para evento (un evento producido por un control que depende de otro control, como un campo de texto con sugerencias de búsqueda) no estaba disponible en el lector de pantalla NVDA, pero la verbalización de sugerencias de búsqueda se hizo posible cuando este complemento añadió este evento. 2. Añade elementos de interfaz de usuario para este complemento, y más concretamente su diálogo de ajustes. 3. Comprueba actualizaciones del complemento si le hemos indicado que lo haga. Autor: Joseph Lee Derechos de copia: Microsoft Windows, Windows 10, Windows API, UI Automation, Microsoft Edge, Universal Windows Platform (UWP) y otras tecnologías relacionadas tienen copyright de Microsoft Corporation. NVDA tiene copyright de NV Access. Descargo de responsabilidad: a pesar del texto del artículo y los conocimientos que contiene, yo (Joseph Lee, el creador del complemento) no trabajo para NV Access ni Microsoft. Llamo a la beta de octubre de 2014 (compilación 9841) vuelo inaugural por varias razones. En primer lugar, es la primera vez donde Microsoft mostró interés en las opiniones de los usuarios. Aunque existieron betas para versiones anteriores de Windows, como Windows 7 y 8.1, Windows 10 es el primer intento de Microsoft de conectar con los usuarios y tomar los comentarios en serio. En segundo lugar, la compilación 9841 (la primera compilación para insiders) marcó el comienzo de Windows como un servicio, un enfoque completamente diferente para mejorar Windows en el que Microsoft quería ofrecer dos cosas: entrega continua y bucle de realimentación, y una configuración unificada que funcione bien con la mayoría de dispositivos. Hubo contratiempos, como las preocupaciones que se generaron en privacidad debido a la telemetría, pero en la mayoría de los casos Windows 10 fue recibido positivamente. En Complementos de NVDA vistos por dentro: Windows 10 App Essentials, veremos cómo se creó este complemento, cómo funciona, y algunas recomendaciones de su autor (yo) relacionadas con prácticas de accesibilidad. También estudiaremos cómo funciona UI Automation a alto nivel, cómo algunas funciones empiezan en forma de complemento y acaban integradas en NVDA, y mucho más. Revisión: diciembre de 2017 Dar soporte a nuevas tecnologías puede ser un reto divertido, especialmente si hablamos de la nueva versión de un sistema operativo que cambia el modo que tiene la gente de realizar ciertas tareas y presenta nuevas formas de mantenerse al día. Este reto es aún mayor cuando se centra en dar soporte a los lectores de pantalla para que funcionen en nuevos sistemas operativos tales como Windows 10, que trae nuevas formas de interactuar con el ordenador, un nuevo conjunto de aplicaciones y tecnologías, y mejoras y retos de accesibilidad. NVDA viene con un soporte sólido para Windows 10, incluyendo Microsoft Edge, el nuevo menú de inicio, navegación en aplicaciones universales y mucho más, todo hecho posible gracias a la colaboración entre los usuarios, Microsoft, NV Access y otros. Parte de este soporte se da gracias al complemento que encontraremos en este artículo. El complemento Windows 10 App Essentials está formado por una extensión global y módulos de aplicación para diversas aplicaciones universales que vienen con Windows 10. Los objetos de Windows 10 (abreviados como WinTenObjs), la porción de extensión global de este complemento, ofrecen soluciones como clases de superposición para controles que se encuentran frecuentemente en Windows 10 y las aplicaciones universales, rastreo de eventos UIA y registro, así como el mecanismo de actualización del complemento. Se puede encontrar más información sobre cómo funciona el actualizador del complemento en el artículo sobre el complemento para Station Playlist Studio, ya que ambos complementos usan el mismo sistema de actualizaciones. Lo único que se hace al apagarlo es desactivar su sistema de comprobación de actualizaciones y eliminar los elementos de interfaz de usuario. Hay otra razón más personal para llamar a la compilación de octubre de 2014 el vuelo inaugural: yo fui uno de los primeros insiders, y debido a mis trabajos con NVDA, decidí que los usuarios de lectores de pantalla debíamos ser tratados con respeto. Esto incluía enviar retroalimentación relacionada con la accesibilidad, conseguir que otros usuarios de lectores de pantalla subieran a bordo del programa Windows Insider, y liberar versiones de desarrollo de NVDA que resolvieran problemas importantes para los Windows insiders. Esto culminó con la publicación del complemento Windows 10 App Essentials en noviembre de 2015 (justo a tiempo de que se liberara la versión 1511 / compilación 10586) que traía soporte para el centro de Windows Insider (actualmente centro de comentarios) y otras soluciones, que se tradujeron en una experiencia magnífica para los usuarios de NVDA al usar Windows 10 y diversas aplicaciones universales. Mi trabajo de la defensa de la accesibilidad continúa hoy en día, especialmente cuando toca asegurarse de que las aplicaciones de terceros son usables para muchos. Para descargar este complemento, visita la sección correspondiente, que encontrarás en el menú superior de nuestra web. El código fuente puede encontrarse en https://github.com/josephsl/wintenApps. Ya que Windows 10 y las aplicaciones universales pertenecen al mundo de UI Automation, es esencial que sepas algunas cosas sobre UIA, que se cubren más adelante. Cuando el complemento se carga, hace tres cosas: El complemento Windows 10 App Essentials se ha construido sobre cuatro pilares: Windows 10 es la "última" gran versión de Windows previsiblemente para el futuro. Nos presenta una forma completamente nueva de mantener un seguimiento de los cambios a través del Windows Insider Program y Windows como servicio (WAAS, un término fantástico para hablar de entrega continua), un nuevo marco de trabajo de desarrollo de aplicaciones, estrategias de unificación en términos de experiencia de usuario a través de dispositivos y un nuevo explorador web. Además, destacan el regreso del viejo estilo del menú inicio, los escritorios virtuales, el centro de actividades para centralizar las notificaciones, una nueva forma de ejecutar utilidades de consola de Linux, y un renovado narrador que sigue introduciendo mejoras. Windows 10 hizo su vuelo inaugural en octubre de 2014. Antes de eso, era conocido como Windows Technical Preview, y tras varias semanas, su nombre cambió al de programa Windows Insider. Entre octubre de 2014 y julio de 2015, cuando se liberó la versión 1507 (compilación 10240), más de cinco millones de usuarios se convirtieron en insiders, probando nuevas compilaciones y aplicaciones, enviando retroalimentación, etc. 