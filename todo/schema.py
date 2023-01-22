instructions =[
    'SET FOREIGN_KEY_CHECKS=0',
    'DROP TABLE IF EXISTS abono',
    'DROP TABLE IF EXISTS citas',
    'DROP TABLE IF EXISTS consulta',
    'DROP TABLE IF EXISTS mat_consulta',
    'DROP TABLE IF EXISTS materiales',
    'DROP TABLE IF EXISTS pagos',
    'DROP TABLE IF EXISTS persona',
    'DROP TABLE IF EXISTS preguntas',
    'DROP TABLE IF EXISTS respuestas',
    'DROP TABLE IF EXISTS rol',
    'DROP TABLE IF EXISTS tipo_pregunta`',
    'DROP TABLE IF EXISTS tratamientos',
    'DROP TABLE IF EXISTS usuarios',
    'SET FOREIGN_KEY_CHECKS=1',
    """
        CREATE TABLE `abono` (
        `id_abono` int(11) NOT NULL AUTO_INCREMENT,
        `fk_id_pago` int(11) DEFAULT NULL,
        `fk_id_paciente` int(11) DEFAULT NULL,
        `nu_nabono` int(11) DEFAULT NULL,
        `nu_monto` int(11) DEFAULT NULL,
        `fh_abono` date DEFAULT NULL,
        PRIMARY KEY (`id_abono`),
        KEY `fk_id_pago` (`fk_id_pago`),
        KEY `fk_id_paciente` (`fk_id_paciente`),
        CONSTRAINT `abono_ibfk_1` FOREIGN KEY (`fk_id_pago`) REFERENCES `pagos` (`id_pago`),
        CONSTRAINT `abono_ibfk_2` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`)
        )
    """
    ,
    """
        CREATE TABLE `citas` (
        `id_cita` int(11) NOT NULL AUTO_INCREMENT,
        `fk_id_paciente` int(11) DEFAULT NULL,
        `fh_cita` date DEFAULT NULL,
        `fk_id_dentista` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_cita`),
        KEY `fk_id_paciente` (`fk_id_paciente`),
        KEY `fk_id_dentista` (`fk_id_dentista`),
        CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`),
        CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`fk_id_dentista`) REFERENCES `usuarios` (`id_usuario`)
        )  
    """
    ,
    """
        CREATE TABLE `consulta` (
        `id_consulta` int(11) NOT NULL AUTO_INCREMENT,
        `fk_id_paciente` int(11) DEFAULT NULL,
        `fk_id_dentista` int(11) DEFAULT NULL,
        `fk_id_tratamiento` int(11) DEFAULT NULL,
        `tx_desc` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        PRIMARY KEY (`id_consulta`),
        KEY `fk_id_paciente` (`fk_id_paciente`),
        KEY `fk_id_dentista` (`fk_id_dentista`),
        KEY `fk_id_tratamiento` (`fk_id_tratamiento`),
        CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`),
        CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`fk_id_dentista`) REFERENCES `usuarios` (`id_usuario`),
        CONSTRAINT `consulta_ibfk_3` FOREIGN KEY (`fk_id_tratamiento`) REFERENCES `tratamientos` (`id_tratamiento`)
        )
    """
    ,
    """
        CREATE TABLE `mat_consulta` (
        `id_matc` int(11) NOT NULL AUTO_INCREMENT,
        `fk_id_material` int(11) DEFAULT NULL,
        `fk_id_consulta` int(11) DEFAULT NULL,
        `nu_cantidad` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_matc`),
        KEY `fk_id_consulta` (`fk_id_consulta`),
        KEY `fk_id_material` (`fk_id_material`),
        CONSTRAINT `mat_consulta_ibfk_1` FOREIGN KEY (`fk_id_consulta`) REFERENCES `consulta` (`id_consulta`),
        CONSTRAINT `mat_consulta_ibfk_2` FOREIGN KEY (`fk_id_material`) REFERENCES `materiales` (`id_material`)
        )
    """
    ,
    """
        CREATE TABLE `materiales` (
        `id_material` int(11) NOT NULL AUTO_INCREMENT,
        `tx_nombre` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `nu_cantidad` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_material`)
        )
    """
    ,
    """
        CREATE TABLE `pagos` (
        `id_pago` int(11) NOT NULL AUTO_INCREMENT,
        `fk_id_paciente` int(11) DEFAULT NULL,
        `nu_total` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_pago`),
        KEY `fk_id_paciente` (`fk_id_paciente`),
        CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`)
        )  
    """
    ,
    """
        CREATE TABLE `persona` (
        `fk_id_usuario` int(11) DEFAULT NULL AUTO_INCREMENT,
        `tx_nombre` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `tx_paterno` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `tx_materno` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `tx_telefono` int(11) DEFAULT NULL,
        `tx_sexo` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        KEY `fk_id_usuario` (`fk_id_usuario`),
        CONSTRAINT `persona_ibfk_1` FOREIGN KEY (`fk_id_usuario`) REFERENCES `usuarios` (`id_usuario`)
        )
    """
    ,
    """
        CREATE TABLE `preguntas` (
        `id_pregunta` int(11) NOT NULL AUTO_INCREMENT,
        `tx_pregunta` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `fk_id_tipo_pregunta` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_pregunta`),
        KEY `fk_id_tipo_pregunta` (`fk_id_tipo_pregunta`),
        CONSTRAINT `preguntas_ibfk_1` FOREIGN KEY (`fk_id_tipo_pregunta`) REFERENCES `tipo_pregunta` (`id_tipo_pregunta`)
        )
    """
    ,
    """
        CREATE TABLE `respuestas` (
        `id_respuesta` int(11) NOT NULL AUTO_INCREMENT,
        `fk_id_pregunta` int(11) DEFAULT NULL,
        `fk_id_paciente` int(11) DEFAULT NULL,
        `fk_id_dentista` int(11) DEFAULT NULL,
        `nu_resp` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_respuesta`),
        KEY `fk_id_pregunta` (`fk_id_pregunta`),
        KEY `fk_id_paciente` (`fk_id_paciente`),
        KEY `fk_id_dentista` (`fk_id_dentista`),
        CONSTRAINT `respuestas_ibfk_1` FOREIGN KEY (`fk_id_pregunta`) REFERENCES `preguntas` (`id_pregunta`),
        CONSTRAINT `respuestas_ibfk_2` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`),
        CONSTRAINT `respuestas_ibfk_3` FOREIGN KEY (`fk_id_dentista`) REFERENCES `usuarios` (`id_usuario`)
        )
    """
    ,
    """
        CREATE TABLE `rol` (
        `id_rol` int(11) NOT NULL,
        `tx_nombre` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        PRIMARY KEY (`id_rol`)
        )
    """
    ,
    """
        CREATE TABLE `tipo_pregunta` (
        `id_tipo_pregunta` int(11) NOT NULL,
        `tx_pregunta` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        PRIMARY KEY (`id_tipo_pregunta`)
        )  
    """
    ,
    """
        CREATE TABLE `tratamientos` (
        `id_tratamiento` int(11) NOT NULL AUTO_INCREMENT,
        `tx_nombre` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `tx_desc` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `nu_precio` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_tratamiento`)
        )
    """
    ,
    """
        CREATE TABLE `usuarios` (
        `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
        `tx_correo` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `tx_password` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
        `fk_id_rol` int(11) DEFAULT NULL,
        PRIMARY KEY (`id_usuario`),
        KEY `fk_id_rol` (`fk_id_rol`),
        CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`fk_id_rol`) REFERENCES `rol` (`id_rol`)
        )
    """
]