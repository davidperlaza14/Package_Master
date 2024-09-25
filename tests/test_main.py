import subprocess
import pytest
from unittest.mock import patch, MagicMock
from src.main import instalar_paquete, actualizar_paquete, desinstalar_paquete, listar_paquetes

@patch('src.main.subprocess.run')
def test_instalar_paquete(mock_subprocess):
    # Configurar el mock para simular una respuesta exitosa de subprocess.run
    mock_subprocess.return_value = MagicMock(stdout='Paquete instalado', stderr='', returncode=0)
    
    # Llamar a la función que queremos probar
    instalar_paquete('requests')
    
    # Verificar que subprocess.run fue llamado con los argumentos correctos
    mock_subprocess.assert_called_once_with(
        ['pip', 'install', 'requests'],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

@patch('src.main.subprocess.run')
def test_actualizar_paquete(mock_subprocess):
    mock_subprocess.return_value = MagicMock(stdout='Paquete actualizado', stderr='', returncode=0)
    
    actualizar_paquete('requests')
    
    mock_subprocess.assert_called_once_with(
        ['pip', 'install', '--upgrade', 'requests'],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

@patch('src.main.subprocess.run')
def test_desinstalar_paquete(mock_subprocess):
    mock_subprocess.return_value = MagicMock(stdout='Paquete desinstalado', stderr='', returncode=0)
    
    desinstalar_paquete('requests')
    
    mock_subprocess.assert_called_once_with(
        ['pip', 'uninstall', '-y', 'requests'],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

@patch('src.main.subprocess.run')
def test_listar_paquetes(mock_subprocess):
    mock_subprocess.return_value = MagicMock(stdout='Paquete1\nPaquete2', stderr='', returncode=0)
    
    listar_paquetes()
    
    mock_subprocess.assert_called_once_with(
        ['pip', 'list'],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
