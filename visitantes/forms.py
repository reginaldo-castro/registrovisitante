from django import forms
from visitantes.models import Visitante

class visitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "setor_visitado", "placa_veiculo",
        ]
        error_messages = {
                "nome_completo": {
                    "required": "O nome completo do visitante é obrigatório para registro"
                },
                "cpf": {
                    "required": "O CPF do visitante é obrigatório para o registro"
                },
                "data_nascimento": {
                    "required": "A data de nascimento do visitante é obrigatório",
                    "invalid": "Por favor, informe um formato válido para a data de nascimento"
                },
                "setor_visitado": {
                    "required": "Por favor, informe o setor a ser visitado"
                }
            }