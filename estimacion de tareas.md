# ATLAS

1. Modelado de la Base de Datos (Modelo)

    Aplicación de Modelos:

        Crear las aplicaciones necesarias:
            assets, categories, locations, purchase_positions, reports, notifications, users, account.
        Considera las relaciones entre las entidades, los campos y los estados de cada modelo.

    Modelos:

        Activo Histórico (Asset):

            Nombre del activo (campo CharField).
            Nombre del activo en inglés (campo CharField, opcional).
            Categoría del activo (relación con un modelo Category).
            Tipo de cantidad (campo ChoiceField con opciones: "Unidades Sueltas", "Cajas", "Contenedores", "Otros").
            Estado del activo (campo ChoiceField con las opciones: "Disponible", "Reservado", "Vendido", "Otro").
            Notas o comentarios (campo TextField).
            Ubicación (relación con un modelo Location).
            Los activos tienen estados cuando aplican a una postura (campo StatusChoices con las opciones AVAILABLE, RESERVED, SOLD, OTHER).
            Los activos pueden ser múltiples y un tenedor puede tener varios activos (relación con un modelo User, que es el tenedor).
            Trazabilidad: Añadir un campo para almacenar un identificador único del activo (como un UUID) para mejorar la trazabilidad y evitar conflictos entre activos similares.
            Historial de estados: Crear un modelo separado para guardar el historial de cambios de estado del activo, lo que permitirá auditar cómo ha cambiado a lo largo del tiempo.
            Cantidad por ubicación: Dividir la cantidad en diferentes ubicaciones dentro de un mismo continente, país o región.

        Comprador (Buyer):

            Relación con el modelo User.
            El comprador realiza "posturas" para comprar activos históricos.
            El comprador puede rechazar tenedores dependiendo del estado del activo.
            El comprador no tiene acceso a los nombres directos de los tenedores.
            Puede ver una lista de activos disponibles y el estado de las posturas.
            Duración de la postura: Agregar campos para definir fechas de inicio y fin de la postura.
            Estado avanzado: Ampliar los estados posibles de una postura para incluir opciones como "En Proceso" o "En Revisión".
            Notas específicas del comprador: Permitir al comprador agregar comentarios o requerimientos específicos para cada postura.

        Intermediario (Intermediary):

            Relación con el modelo User, es el rol que gestiona el intercambio entre comprador y tenedor.
            Este rol tiene permisos especiales de administración de activos y posturas.

        Postura de Compra/Venta (PurchasePosition):

            Relación con el comprador (Buyer).
            Relación con el activo (Asset).
            Cantidad de activos que se desean comprar/vender.
            Precio por unidad o por cantidad de activo.
            Estado de la postura (campo ChoiceField con las opciones: "Abierta", "Cerrada", "Cancelada").
            La postura tiene un límite de cantidad (ej., mínimo y máximo de unidades, cajas o contenedores).
            Un comprador puede hacer múltiples posturas.
            
        Categoría (Category):

            Definir categorías predefinidas de activos históricos.

        Ubicación (Location):

            Referencia de ubicación.
            Continente, país y descripción de la ubicación (usando las opciones de continente como AS, NA, CA, etc.).

2. Consideraciones de Roles y Permisos:

    Tenedor (Asset Owner):

        Permiso de añadir, modificar y eliminar activos.
        Ver las posturas a las que ha aplicado y el estado del activo.
        Cambiar el estado de sus activos (por ejemplo, de "Disponible" a "Reservado").
        Permitir ver estadísticas sobre sus activos (cantidad vendida, reservada, rechazada).
        Agregar permisos específicos para determinar quién puede ver las notas relacionadas con un activo.

    Comprador (Buyer):

        Puede hacer posturas para comprar activos.
        Puede rechazar tenedores basados en el estado del activo.
        Puede ver los activos disponibles y sus estados.
        No puede acceder a los detalles de los tenedores, pero puede interactuar con ellos a través de posturas.

    Intermediario (Intermediary):

        Permisos de administración para gestionar posturas, compradores y tenedores.
        Gestionar la negociación entre compradores y tenedores.
        Definir permisos granulares para el intermediario, como la capacidad de:
            Editar las posturas solo si el comprador/tenedor lo permite explícitamente.
            Gestionar un sistema de resolución de conflictos entre compradores y tenedores.
        Añadir la capacidad de generar reportes personalizados basados en las transacciones realizadas.

    Validaciones y reglas de negocio
        Mejorar la coherencia de los datos con validaciones adicionales:

        Validar las posturas:
            Asegurar que las cantidades mínimas y máximas de una postura sean respetadas por los activos asignados.
            Validar que un activo no pueda estar asociado simultáneamente con dos posturas en conflicto (por ejemplo, si ya está reservado en una postura, no puede ser reservado en otra).
        Estados de activos:
            Estados personalizados: Definir subestados específicos para "Other" y validar su uso con reglas claras (por ejemplo: "Dañado", "Pendiente de Reparación").

3. Vistas basadas en clases (CBVs)

    Views (Vistas):

        Activo Histórico:

            Vista para listar los activos disponibles y sus detalles.
            Vista para crear, editar y eliminar activos históricos (solo para tenedores).

        Postura de Compra:

            Vista para crear posturas (solo para compradores).
            Vista para ver las posturas activas de un comprador.
            Vista para aceptar o rechazar posturas dependiendo del estado del activo.

        Dashboard del Intermediario:

            Vista para gestionar las interacciones entre compradores y tenedores, ver el estado de las posturas, etc.
            Usuarios (Perfil de Usuario):

        Vista para que los usuarios puedan gestionar su perfil (tanto tenedores como compradores).

4. Templates (Plantillas)

    Plantillas para la vista de listar activos históricos con detalles (nombre, estado, ubicación, etc.).
    Plantillas para la vista de posturas donde los compradores pueden hacer nuevas posturas, ver las existentes y su estado.
    Plantillas para la vista de dashboard del intermediario donde se gestionan las posturas y se facilita la comunicación entre compradores y tenedores.
    Crear plantillas para un sistema de mensajes entre compradores y tenedores, facilitando la comunicación.

5. URLs y Routing:

    Definir las URLs para las vistas que hemos mencionado:
        /assets/ para listar los activos históricos.
        /purchase-positions/ para gestionar posturas de compra/venta.
        /users/profile/ para que los usuarios gestionen sus perfiles.
        /intermediary/dashboard/ para la vista de gestión de posturas para el intermediario.

6. Signals y Eventos

    Crear señales para manejar el cambio de estado de un activo cuando un tenedor aplica a una postura.
    Generar notificaciones cuando un comprador realiza una postura que afecta a un tenedor.
    Actualizar la cantidad necesaria de activos para cumplir con la cuota de una postura (en caso de que se haya excedido o se haya reducido).
    Cambio de estado del activo:
        Enviar notificaciones automáticas tanto al comprador como al tenedor cuando un activo cambie de estado.
    Vencimiento de posturas:
        Implementar un evento que cierre automáticamente las posturas una vez alcanzada su fecha de vencimiento.
    Posturas excedentes:
        Notificar al comprador y al intermediario cuando las posturas excedan la cantidad máxima permitida, indicando qué activos adicionales ha sido agregados pero pueden no ser tomados en cuenta.

7. Consideraciones Técnicas:

    Autenticación y Permisos:

        Usar Django Rest Framework (DRF) o Django simple para la autenticación de usuarios y roles.
        Gestionar permisos basados en roles de usuario (Tenedor, Comprador, Intermediario).

    Notificaciones:

        Implementar un sistema de notificaciones (por ejemplo, con Django Signals o Celery) para alertar a los usuarios cuando un activo cambia de estado o cuando un comprador hace una postura.
        Tipos de notificaciones:
            Agregar opciones para enviar notificaciones por correo electrónico y a través de la plataforma (in-app).
            Implementar alertas para recordar a los usuarios sobre posturas cercanas a su fecha de vencimiento.
        Permitir a los usuarios configurar las preferencias de notificación según su rol (por ejemplo, el tenedor podría recibir notificaciones solo cuando su activo sea vendido o reservado).

    Validación de Datos:

        Validar las cantidades en las posturas (mínimos y máximos).
        Validar la coherencia de los datos cuando se cambia el estado de un activo o se realiza una nueva postura.
        Documentar casos de uso para señales, vistas y templates.

    Proporcionar manuales básicos y avanzados para cada rol.

8. Apps externas:

    Integrar aplicaciones como django_otp, django_recaptcha, axes para mejorar la seguridad.
    Usar import_export para permitir la importación/exportación de datos.
    Usar django_filters para filtrar activos y posturas en las vistas.
    Implementar un sistema de auditoría con auditlog.

| Tarea Principal                       | Sub-Tarea                                                 | Responsable     | Tiempo Estimado | Estado        |
|---------------------------------------|-----------------------------------------------------------|-----------------|-----------------|---------------|
| 1. Modelado de la Base de Datos       | Crear modelos para Asset, Buyer, Intermediary             | Persona 1       | 8 horas         | En progreso   |
|                                       | Crear modelos para Category, Location, PurchasePosition   | Persona 2       | 8 horas         | En progreso   |
|                                       | Definir relaciones entre modelos y validar datos          | Persona 3       | 4 horas         | En progreso   |
|                                       | Crear migraciones y aplicar a la base de datos            | Persona 3       | 2 horas         | En progreso   |
| 2. Roles y Permisos                   | Configurar permisos para Tenedor, Comprador               | Persona 1       | 8 horas         | En progreso   |
|                                       | Configurar permisos para Intermediario                    | Persona 2       | 8 horas         | En progreso   |
|                                       | Implementar validaciones y reglas de negocio              | Persona 3       | 24 horas        | En progreso   |
| 3. Vistas (CBVs)                      | Implementar vistas para listar activos                    | Persona 1       | 24 horas        | En progreso   |
|                                       | Implementar vistas para posturas de compra                | Persona 2       | 24 horas        | En progreso   |
|                                       | Crear dashboard del Intermediario                         | Persona 3       | 24 horas        | En progreso   |
| 4. Templates                          | Diseñar plantilla para listar activos                     | Persona 1       | 16 horas        | En progreso   |
|                                       | Diseñar plantilla para posturas                           | Persona 2       | 16 horas        | En progreso   |
|                                       | Diseñar dashboard para el intermediario                   | Persona 3       | 32 horas        | En progreso   |
| 5. URLs y Routing                     | Configurar URLs para las vistas de activos                | Persona 1       | 4 horas         | En progreso   |
|                                       | Configurar URLs para las posturas                         | Persona 2       | 4 horas         | En progreso   |
|                                       | Configurar URLs para el dashboard del intermediario       | Persona 3       | 4 horas         | En progreso   |
| 6. Signals y Eventos                  | Implementar señales para cambios de estado                | Persona 1       | 24 horas        | En progreso   |
|                                       | Crear notificaciones de cambios y vencimientos            | Persona 2       | 32 horas        | En progreso   |
|                                       | Validar eventos para posturas excedentes                  | Persona 3       | 16 horas        | En progreso   |
| 7. Consideraciones Técnicas           | Configurar autenticación                                  | Persona 1       | 32 horas        | En progreso   |
|                                       | Implementar notificaciones in-app                         | Persona 2       | 32 horas        | En progreso   |
|                                       | Validar coherencia de datos y estados                     | Persona 3       | 40 horas        | En progreso   |
| 8. Integración de Apps externas       | Configurar django_otp y seguridad                         | Persona 1       | 24 horas        | En progreso   |
|                                       | Implementar filtros y auditoría                           | Persona 2       | 16 horas        | En progreso   |
|                                       | Probar import/export y recaptcha                          | Persona 3       | 8 horas         | En progreso   |

Total horas: 434

Persona 1 (Yo):
    Dias:       140 horas ÷ 8 horas/dia = 17.5 dias
    Semanas:    17.5 dias ÷ 5 dias/semana = 4 semanas

Persona 2 (85k/h):
    Dias:       140 h ÷ 8 h/d = 17.5 dias
    Semanas:    17.5 dias ÷ 5 dias/semana = 4 semanas
    Valor apx: 85.000 * 140 = 11.900.000
    Valor apx 4 semanas: 13.600.000

Persona 3 (80k/h):
    Dias:       154 h ÷ 8 h/d = 19.25 dias
    Semanas:    19.25 dias ÷ 5 dias/semana = 4 semanas
    Valor: 80.000 * 154 = 12.320.000
    Valor apx 4 semanas: 12.800.000

----
Definición de tareas, tiempos, modelado de la base de datos, flujos, modelos, vistas, templates, urls, consideraciones

Tengo tres tipos de usuario

- Tenedor (Quien posee los activos históricos)
- Comprador (Quien realiza ponencias y desea comprar activos históricos)
- Intermediario (Quien se encarga de conectar Comprador y Tenedor), este somos nosotros, que ofrecemos todos los servicios para un intercambio seguro, pero hay roles y permisos

Activos Históricos

- Nombre del activo
- Nombre del activo en ingles (opcional)
- Categoría del activo (categorías pre definidas)
- Tipo de cantidad (Unidades Sueltas, Cajas, Contenedores, Otros) por defecto cajas
- Estado del activo
- Notas o Comentarios
- Ubicación (Referencia, Continente (ASIA = "AS", _("Asia")
        NORTH_AMERICA = "NA", _("North America")
        CENTRAL_AMERICA = "CA", _("Central America")
        SOUTH_AMERICA = "SA", _("South America")
        AFRICA = "AF",_("Africa")
        ANTARCTICA = "AN", _("Antarctica")
        EUROPE = "EU",_("Europe")
        OCEANIA = "OC", _("Oceania")) País y Descripción)
- Tienen estados cuando aplican a una postura o la postura finaliza:
class StatusChoices(models.TextChoices):
        AVAILABLE = "A",_("Available")
        RESERVED = "R",_("Reserved")
        SOLD = "S", _("Sold")
        OTHER = "O",_("Other")
Notas:
Disponible: El activo no se ha vendido, No se encuentra en una postura
Reservado: El activo se encuentra en una o más posturas
Sold: Una postura a finalizado con éxito y el activo ha sido vendido
Other: Hay algún inconveniente con el activo y no puede ser colocado en ninguna postura, vendido o estar disponible (acá se tiene que especificar qué tipo de estado nuevo va a tener)

Un solo tenedor puede tener el activo 4 por ejemplo 1 contenedor en Sur America con Ref 1 y 50 cajas en Sur America con Ref 2

Comprador:

- Realiza posturas, las posturas funcionan como un sistema de "Compra/Venta", el dice "Estoy comprando [CANTIDAD] de [TIPO DE CANTIDAD] del [ACTIVO] a un precio [PRECIO] en [PAIS]"
- El comprador puede rechazar tenedores dependiendo del estado del activo del tenedor
- El comprador no tiene acceso a nombres directos de tenedores
- El comprador puede ver una lista de activos y saber si se cumple la cuota de la cantidad

Hay que manejar los signals para:

- Cambio de estados cuando el tenedor aplique a una postura y que le aparezca la lista de las posturas a las que ha aplicado
- Cambio en la cantidad necesaria para cumplir la cuota de la postura (pueden haber excedentes, por ejemplo la postura pide 5 cajas cómo mínimo, pero como máximo acepta 20, pero puede seguir aceptando)

resumiendo
Apps:
assets, categories, locations, purchase_positions, reports, notifications, users, account
3d Apps:
auditlog, import_export, axes, django_filters, django_otp, django_recaptcha, encrypted_model_fields, honeypot, two_factor
