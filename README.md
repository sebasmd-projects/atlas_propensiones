# Atlas

## Dependencias

### Terceros

- **auditlog**: Permite llevar un registro de auditoría de los cambios en los modelos, especialmente útil para rastrear accesos y modificaciones en los registros de usuario.
- **axes**: Protege la aplicación contra ataques de fuerza bruta bloqueando los intentos de inicio de sesión fallidos repetidos.
- **corsheaders**: Middleware para manejar CORS en Django, necesario para permitir solicitudes desde diferentes orígenes.
- **rest_framework**: Conjunto de herramientas para construir APIs RESTful en Django. Es fundamental para construir endpoints.
- **rest_framework.authtoken**: Permite la autenticación basada en tokens, útil para proporcionar acceso a la API mediante tokens.
- **rest_framework_simplejwt**: Proporciona autenticación basada en JSON Web Tokens (JWT), una forma segura de autenticación sin estado para APIs RESTful.
- **drf_yasg**: Generador de documentación Swagger para APIs construidas con Django REST Framework, lo que facilita la creación de documentación interactiva para tus endpoints.
- **honeypot**: Añade campos invisibles a los formularios para atrapar bots y reducir el spam en los formularios de contacto.
- **django_recaptcha**: Implementa Google reCAPTCHA en formularios de Django para verificar que los envíos no sean de bots.
- **import_export**: Facilita la importación y exportación de datos en formatos como CSV y Excel desde el admin de Django. Puede ser útil para manejar grandes volúmenes de datos de clientes.
- **parler**: Proporciona funcionalidad de internacionalización para modelos Django, permitiendo el manejo de contenido en varios idiomas.
- **rosetta**: Herramienta para la traducción fácil de archivos `.po` en Django, facilita la traducción del contenido dentro de la aplicación.

## Estructura DevOps

1. Estructura de Ramas
    main: La rama de producción, solo debe contener código aprobado y probado.
    develop: La rama de desarrollo principal. Aquí se integran nuevas funcionalidades antes de enviarlas a producción.
    feature/: Ramas para cada nueva funcionalidad, nombradas según el objetivo, por ejemplo, feature/authentication o feature/customer-crud.
    bugfix/: Ramas específicas para solucionar bugs detectados en producción o desarrollo, por ejemplo, bugfix/form-validation.
    hotfix/: Para corregir problemas críticos en producción, por ejemplo, hotfix/security-fix.
    release/: Ramas dedicadas para preparar una nueva versión antes de ser liberada en producción, por ejemplo, release/v1.0.

2. Convenciones para Commits
    version: para definir un release.
    feat: para nuevas funcionalidades.
    fix: para arreglos de bugs.
    refactor: para refactorización de código sin cambios funcionales.
    docs: para cambios en documentación.
    test: para cambios en pruebas o nuevas pruebas.
    config: para cambios en configuraciones.
    chore: para tareas de mantenimiento (actualización de dependencias, etc.).
        Ejemplo: feat: agregar endpoint de registro en CRM.

3. Workflow de Git
    Creación de rama:
        Crea una rama a partir de develop para cada nueva funcionalidad o corrección.
    Commits y Push:
        Realiza commits con frecuencia siguiendo las convenciones establecidas.
        Haz push de la rama cuando los cambios estén listos para revisión.
    Pull Requests (PR):
        Cuando termines una funcionalidad, abre un Pull Request (PR) hacia la rama develop o hacia la rama correspondiente (release o main en caso de hotfix).
        Revisa los PR de tus compañeros para asegurar un flujo de revisión y control de calidad.
    Merge:
        Después de que un PR sea aprobado, haz merge a develop.
        Para releases, usa la rama release/x.x, y haz merge a main solo después de pruebas exhaustivas.

4. Pipeline de CI/CD (Integración y Despliegue Continuo)
    Ramas de feature/* y bugfix/*: Ejecuta pruebas unitarias y de integración.
    Rama develop: Despliega automáticamente a un entorno de desarrollo y ejecuta pruebas de integración adicionales.
    Rama release/*: Despliega a un entorno de preproducción para realizar pruebas de aceptación.
    Rama main: Despliega automáticamente a producción solo después de que todos los tests hayan pasado.
