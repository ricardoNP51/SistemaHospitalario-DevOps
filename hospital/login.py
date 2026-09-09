"""Validación de campos de un formulario; no autentica usuarios."""


def validar_campos_login(usuario: str, clave: str) -> bool:
    """Indica si ambos campos contienen texto antes de enviarlos a un backend."""
    return bool(usuario.strip()) and bool(clave.strip())
