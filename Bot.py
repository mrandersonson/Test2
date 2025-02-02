from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Токен вашего бота (замените на ваш реальный токен)
TOKEN = '6972062873:AAGOC-NQ-tt1w4FSahvGFyIRUBy8EeSRtf4'

# Полная структура с уникальными именами для всех директорий
PRODUCTS = {
    'Main_A': {  # Основная директория
        'Alpha': {  # Поддиректория
            'Sub_Alpha_1': {  # Подподдиректория
                'Extra_Alpha_1':
                'https://example.com/Main_A/Alpha/Sub_Alpha_1/Extra_Alpha_1',
                'Extra_Alpha_2':
                'https://example.com/Main_A/Alpha/Sub_Alpha_1/Extra_Alpha_2',
                'Extra_Alpha_3':
                'https://example.com/Main_A/Alpha/Sub_Alpha_1/Extra_Alpha_3',
                'Extra_Alpha_4':
                'https://example.com/Main_A/Alpha/Sub_Alpha_1/Extra_Alpha_4',
                'Extra_Alpha_5':
                'https://example.com/Main_A/Alpha/Sub_Alpha_1/Extra_Alpha_5'
            },
            'Sub_Alpha_2': {  # Подподдиректория
                'Extra_Alpha_6':
                'https://example.com/Main_A/Alpha/Sub_Alpha_2/Extra_Alpha_6',
                'Extra_Alpha_7':
                'https://example.com/Main_A/Alpha/Sub_Alpha_2/Extra_Alpha_7',
                'Extra_Alpha_8':
                'https://example.com/Main_A/Alpha/Sub_Alpha_2/Extra_Alpha_8',
                'Extra_Alpha_9':
                'https://example.com/Main_A/Alpha/Sub_Alpha_2/Extra_Alpha_9',
                'Extra_Alpha_10':
                'https://example.com/Main_A/Alpha/Sub_Alpha_2/Extra_Alpha_10'
            },
            'Sub_Alpha_3': {  # Подподдиректория
                'Extra_Alpha_11':
                'https://example.com/Main_A/Alpha/Sub_Alpha_3/Extra_Alpha_11',
                'Extra_Alpha_12':
                'https://example.com/Main_A/Alpha/Sub_Alpha_3/Extra_Alpha_12',
                'Extra_Alpha_13':
                'https://example.com/Main_A/Alpha/Sub_Alpha_3/Extra_Alpha_13',
                'Extra_Alpha_14':
                'https://example.com/Main_A/Alpha/Sub_Alpha_3/Extra_Alpha_14',
                'Extra_Alpha_15':
                'https://example.com/Main_A/Alpha/Sub_Alpha_3/Extra_Alpha_15'
            },
            'Sub_Alpha_4': {  # Подподдиректория
                'Extra_Alpha_16':
                'https://example.com/Main_A/Alpha/Sub_Alpha_4/Extra_Alpha_16',
                'Extra_Alpha_17':
                'https://example.com/Main_A/Alpha/Sub_Alpha_4/Extra_Alpha_17',
                'Extra_Alpha_18':
                'https://example.com/Main_A/Alpha/Sub_Alpha_4/Extra_Alpha_18',
                'Extra_Alpha_19':
                'https://example.com/Main_A/Alpha/Sub_Alpha_4/Extra_Alpha_19',
                'Extra_Alpha_20':
                'https://example.com/Main_A/Alpha/Sub_Alpha_4/Extra_Alpha_20'
            },
            'Sub_Alpha_5': {  # Подподдиректория
                'Extra_Alpha_21':
                'https://example.com/Main_A/Alpha/Sub_Alpha_5/Extra_Alpha_21',
                'Extra_Alpha_22':
                'https://example.com/Main_A/Alpha/Sub_Alpha_5/Extra_Alpha_22',
                'Extra_Alpha_23':
                'https://example.com/Main_A/Alpha/Sub_Alpha_5/Extra_Alpha_23',
                'Extra_Alpha_24':
                'https://example.com/Main_A/Alpha/Sub_Alpha_5/Extra_Alpha_24',
                'Extra_Alpha_25':
                'https://example.com/Main_A/Alpha/Sub_Alpha_5/Extra_Alpha_25'
            }
        },
        'Beta': {  # Поддиректория
            'Sub_Beta_1': {  # Подподдиректория
                'Extra_Beta_1':
                'https://example.com/Main_A/Beta/Sub_Beta_1/Extra_Beta_1',
                'Extra_Beta_2':
                'https://example.com/Main_A/Beta/Sub_Beta_1/Extra_Beta_2',
                'Extra_Beta_3':
                'https://example.com/Main_A/Beta/Sub_Beta_1/Extra_Beta_3',
                'Extra_Beta_4':
                'https://example.com/Main_A/Beta/Sub_Beta_1/Extra_Beta_4',
                'Extra_Beta_5':
                'https://example.com/Main_A/Beta/Sub_Beta_1/Extra_Beta_5'
            },
            'Sub_Beta_2': {  # Подподдиректория
                'Extra_Beta_6':
                'https://example.com/Main_A/Beta/Sub_Beta_2/Extra_Beta_6',
                'Extra_Beta_7':
                'https://example.com/Main_A/Beta/Sub_Beta_2/Extra_Beta_7',
                'Extra_Beta_8':
                'https://example.com/Main_A/Beta/Sub_Beta_2/Extra_Beta_8',
                'Extra_Beta_9':
                'https://example.com/Main_A/Beta/Sub_Beta_2/Extra_Beta_9',
                'Extra_Beta_10':
                'https://example.com/Main_A/Beta/Sub_Beta_2/Extra_Beta_10'
            },
            'Sub_Beta_3': {  # Подподдиректория
                'Extra_Beta_11':
                'https://example.com/Main_A/Beta/Sub_Beta_3/Extra_Beta_11',
                'Extra_Beta_12':
                'https://example.com/Main_A/Beta/Sub_Beta_3/Extra_Beta_12',
                'Extra_Beta_13':
                'https://example.com/Main_A/Beta/Sub_Beta_3/Extra_Beta_13',
                'Extra_Beta_14':
                'https://example.com/Main_A/Beta/Sub_Beta_3/Extra_Beta_14',
                'Extra_Beta_15':
                'https://example.com/Main_A/Beta/Sub_Beta_3/Extra_Beta_15'
            },
            'Sub_Beta_4': {  # Подподдиректория
                'Extra_Beta_16':
                'https://example.com/Main_A/Beta/Sub_Beta_4/Extra_Beta_16',
                'Extra_Beta_17':
                'https://example.com/Main_A/Beta/Sub_Beta_4/Extra_Beta_17',
                'Extra_Beta_18':
                'https://example.com/Main_A/Beta/Sub_Beta_4/Extra_Beta_18',
                'Extra_Beta_19':
                'https://example.com/Main_A/Beta/Sub_Beta_4/Extra_Beta_19',
                'Extra_Beta_20':
                'https://example.com/Main_A/Beta/Sub_Beta_4/Extra_Beta_20'
            },
            'Sub_Beta_5': {  # Подподдиректория
                'Extra_Beta_21':
                'https://example.com/Main_A/Beta/Sub_Beta_5/Extra_Beta_21',
                'Extra_Beta_22':
                'https://example.com/Main_A/Beta/Sub_Beta_5/Extra_Beta_22',
                'Extra_Beta_23':
                'https://example.com/Main_A/Beta/Sub_Beta_5/Extra_Beta_23',
                'Extra_Beta_24':
                'https://example.com/Main_A/Beta/Sub_Beta_5/Extra_Beta_24',
                'Extra_Beta_25':
                'https://example.com/Main_A/Beta/Sub_Beta_5/Extra_Beta_25'
            }
        },
        # Добавьте остальные поддиректории аналогично...
        'Gamma': {},
        'Delta': {},
        'Epsilon': {},
        'Zeta': {},
        'Eta': {},
        'Theta': {},
        'Iota': {}
    },
    'Main_B': {  # Основная директория
        'Kappa': {  # Поддиректория
            'Sub_Kappa_1': {  # Подподдиректория
                'Extra_Kappa_1':
                'https://example.com/Main_B/Kappa/Sub_Kappa_1/Extra_Kappa_1',
                'Extra_Kappa_2':
                'https://example.com/Main_B/Kappa/Sub_Kappa_1/Extra_Kappa_2',
                'Extra_Kappa_3':
                'https://example.com/Main_B/Kappa/Sub_Kappa_1/Extra_Kappa_3',
                'Extra_Kappa_4':
                'https://example.com/Main_B/Kappa/Sub_Kappa_1/Extra_Kappa_4',
                'Extra_Kappa_5':
                'https://example.com/Main_B/Kappa/Sub_Kappa_1/Extra_Kappa_5'
            },
            'Sub_Kappa_2': {  # Подподдиректория
                'Extra_Kappa_6':
                'https://example.com/Main_B/Kappa/Sub_Kappa_2/Extra_Kappa_6',
                'Extra_Kappa_7':
                'https://example.com/Main_B/Kappa/Sub_Kappa_2/Extra_Kappa_7',
                'Extra_Kappa_8':
                'https://example.com/Main_B/Kappa/Sub_Kappa_2/Extra_Kappa_8',
                'Extra_Kappa_9':
                'https://example.com/Main_B/Kappa/Sub_Kappa_2/Extra_Kappa_9',
                'Extra_Kappa_10':
                'https://example.com/Main_B/Kappa/Sub_Kappa_2/Extra_Kappa_10'
            },
            'Sub_Kappa_3': {  # Подподдиректория
                'Extra_Kappa_11':
                'https://example.com/Main_B/Kappa/Sub_Kappa_3/Extra_Kappa_11',
                'Extra_Kappa_12':
                'https://example.com/Main_B/Kappa/Sub_Kappa_3/Extra_Kappa_12',
                'Extra_Kappa_13':
                'https://example.com/Main_B/Kappa/Sub_Kappa_3/Extra_Kappa_13',
                'Extra_Kappa_14':
                'https://example.com/Main_B/Kappa/Sub_Kappa_3/Extra_Kappa_14',
                'Extra_Kappa_15':
                'https://example.com/Main_B/Kappa/Sub_Kappa_3/Extra_Kappa_15'
            },
            'Sub_Kappa_4': {  # Подподдиректория
                'Extra_Kappa_16':
                'https://example.com/Main_B/Kappa/Sub_Kappa_4/Extra_Kappa_16',
                'Extra_Kappa_17':
                'https://example.com/Main_B/Kappa/Sub_Kappa_4/Extra_Kappa_17',
                'Extra_Kappa_18':
                'https://example.com/Main_B/Kappa/Sub_Kappa_4/Extra_Kappa_18',
                'Extra_Kappa_19':
                'https://example.com/Main_B/Kappa/Sub_Kappa_4/Extra_Kappa_19',
                'Extra_Kappa_20':
                'https://example.com/Main_B/Kappa/Sub_Kappa_4/Extra_Kappa_20'
            },
            'Sub_Kappa_5': {  # Подподдиректория
                'Extra_Kappa_21':
                'https://example.com/Main_B/Kappa/Sub_Kappa_5/Extra_Kappa_21',
                'Extra_Kappa_22':
                'https://example.com/Main_B/Kappa/Sub_Kappa_5/Extra_Kappa_22',
                'Extra_Kappa_23':
                'https://example.com/Main_B/Kappa/Sub_Kappa_5/Extra_Kappa_23',
                'Extra_Kappa_24':
                'https://example.com/Main_B/Kappa/Sub_Kappa_5/Extra_Kappa_24',
                'Extra_Kappa_25':
                'https://example.com/Main_B/Kappa/Sub_Kappa_5/Extra_Kappa_25'
            }
        },
        # Добавьте остальные поддиректории аналогично...
        'Lambda': {},
        'Mu': {},
        'Nu': {},
        'Xi': {},
        'Omicron': {},
        'Pi': {},
        'Rho': {},
        'Sigma': {},
        'Lambda': {  # Поддиректория
            'Sub_Lambda_1': {  # Подподдиректория
                'Extra_Lambda_1':
                'https://example.com/Main_B/Lambda/Sub_Lambda_1/Extra_Lambda_1',
                'Extra_Lambda_2':
                'https://example.com/Main_B/Lambda/Sub_Lambda_1/Extra_Lambda_2',
                'Extra_Lambda_3':
                'https://example.com/Main_B/Lambda/Sub_Lambda_1/Extra_Lambda_3',
                'Extra_Lambda_4':
                'https://example.com/Main_B/Lambda/Sub_Lambda_1/Extra_Lambda_4',
                'Extra_Lambda_5':
                'https://example.com/Main_B/Lambda/Sub_Lambda_1/Extra_Lambda_5'
            },
            'Sub_Lambda_2': {  # Подподдиректория
                'Extra_Lambda_6':
                'https://example.com/Main_B/Lambda/Sub_Lambda_2/Extra_Lambda_6',
                'Extra_Lambda_7':
                'https://example.com/Main_B/Lambda/Sub_Lambda_2/Extra_Lambda_7',
                'Extra_Lambda_8':
                'https://example.com/Main_B/Lambda/Sub_Lambda_2/Extra_Lambda_8',
                'Extra_Lambda_9':
                'https://example.com/Main_B/Lambda/Sub_Lambda_2/Extra_Lambda_9',
                'Extra_Lambda_10':
                'https://example.com/Main_B/Lambda/Sub_Lambda_2/Extra_Lambda_10'
            },
            'Sub_Lambda_3': {  # Подподдиректория
                'Extra_Lambda_11':
                'https://example.com/Main_B/Lambda/Sub_Lambda_3/Extra_Lambda_11',
                'Extra_Lambda_12':
                'https://example.com/Main_B/Lambda/Sub_Lambda_3/Extra_Lambda_12',
                'Extra_Lambda_13':
                'https://example.com/Main_B/Lambda/Sub_Lambda_3/Extra_Lambda_13',
                'Extra_Lambda_14':
                'https://example.com/Main_B/Lambda/Sub_Lambda_3/Extra_Lambda_14',
                'Extra_Lambda_15':
                'https://example.com/Main_B/Lambda/Sub_Lambda_3/Extra_Lambda_15'
            },
            'Sub_Lambda_4': {  # Подподдиректория
                'Extra_Lambda_16':
                'https://example.com/Main_B/Lambda/Sub_Lambda_4/Extra_Lambda_16',
                'Extra_Lambda_17':
                'https://example.com/Main_B/Lambda/Sub_Lambda_4/Extra_Lambda_17',
                'Extra_Lambda_18':
                'https://example.com/Main_B/Lambda/Sub_Lambda_4/Extra_Lambda_18',
                'Extra_Lambda_19':
                'https://example.com/Main_B/Lambda/Sub_Lambda_4/Extra_Lambda_19',
                'Extra_Lambda_20':
                'https://example.com/Main_B/Lambda/Sub_Lambda_4/Extra_Lambda_20'
            },
            'Sub_Lambda_5': {  # Подподдиректория
                'Extra_Lambda_21':
                'https://example.com/Main_B/Lambda/Sub_Lambda_5/Extra_Lambda_21',
                'Extra_Lambda_22':
                'https://example.com/Main_B/Lambda/Sub_Lambda_5/Extra_Lambda_22',
                'Extra_Lambda_23':
                'https://example.com/Main_B/Lambda/Sub_Lambda_5/Extra_Lambda_23',
                'Extra_Lambda_24':
                'https://example.com/Main_B/Lambda/Sub_Lambda_5/Extra_Lambda_24',
                'Extra_Lambda_25':
                'https://example.com/Main_B/Lambda/Sub_Lambda_5/Extra_Lambda_25'
            }
        },
        'Mu': {  # Поддиректория
            'Sub_Mu_1': {  # Подподдиректория
                'Extra_Mu_1':
                'https://example.com/Main_B/Mu/Sub_Mu_1/Extra_Mu_1',
                'Extra_Mu_2':
                'https://example.com/Main_B/Mu/Sub_Mu_1/Extra_Mu_2',
                'Extra_Mu_3':
                'https://example.com/Main_B/Mu/Sub_Mu_1/Extra_Mu_3',
                'Extra_Mu_4':
                'https://example.com/Main_B/Mu/Sub_Mu_1/Extra_Mu_4',
                'Extra_Mu_5':
                'https://example.com/Main_B/Mu/Sub_Mu_1/Extra_Mu_5'
            },
            'Sub_Mu_2': {  # Подподдиректория
                'Extra_Mu_6':
                'https://example.com/Main_B/Mu/Sub_Mu_2/Extra_Mu_6',
                'Extra_Mu_7':
                'https://example.com/Main_B/Mu/Sub_Mu_2/Extra_Mu_7',
                'Extra_Mu_8':
                'https://example.com/Main_B/Mu/Sub_Mu_2/Extra_Mu_8',
                'Extra_Mu_9':
                'https://example.com/Main_B/Mu/Sub_Mu_2/Extra_Mu_9',
                'Extra_Mu_10':
                'https://example.com/Main_B/Mu/Sub_Mu_2/Extra_Mu_10'
            },
            'Sub_Mu_3': {  # Подподдиректория
                'Extra_Mu_11':
                'https://example.com/Main_B/Mu/Sub_Mu_3/Extra_Mu_11',
                'Extra_Mu_12':
                'https://example.com/Main_B/Mu/Sub_Mu_3/Extra_Mu_12',
                'Extra_Mu_13':
                'https://example.com/Main_B/Mu/Sub_Mu_3/Extra_Mu_13',
                'Extra_Mu_14':
                'https://example.com/Main_B/Mu/Sub_Mu_3/Extra_Mu_14',
                'Extra_Mu_15':
                'https://example.com/Main_B/Mu/Sub_Mu_3/Extra_Mu_15'
            },
            'Sub_Mu_4': {  # Подподдиректория
                'Extra_Mu_16':
                'https://example.com/Main_B/Mu/Sub_Mu_4/Extra_Mu_16',
                'Extra_Mu_17':
                'https://example.com/Main_B/Mu/Sub_Mu_4/Extra_Mu_17',
                'Extra_Mu_18':
                'https://example.com/Main_B/Mu/Sub_Mu_4/Extra_Mu_18',
                'Extra_Mu_19':
                'https://example.com/Main_B/Mu/Sub_Mu_4/Extra_Mu_19',
                'Extra_Mu_20':
                'https://example.com/Main_B/Mu/Sub_Mu_4/Extra_Mu_20'
            },
            'Sub_Mu_5': {  # Подподдиректория
                'Extra_Mu_21':
                'https://example.com/Main_B/Mu/Sub_Mu_5/Extra_Mu_21',
                'Extra_Mu_22':
                'https://example.com/Main_B/Mu/Sub_Mu_5/Extra_Mu_22',
                'Extra_Mu_23':
                'https://example.com/Main_B/Mu/Sub_Mu_5/Extra_Mu_23',
                'Extra_Mu_24':
                'https://example.com/Main_B/Mu/Sub_Mu_5/Extra_Mu_24',
                'Extra_Mu_25':
                'https://example.com/Main_B/Mu/Sub_Mu_5/Extra_Mu_25'
            }
        },
        'Nu': {  # Поддиректория
            'Sub_Nu_1': {  # Подподдиректория
                'Extra_Nu_1':
                'https://example.com/Main_B/Nu/Sub_Nu_1/Extra_Nu_1',
                'Extra_Nu_2':
                'https://example.com/Main_B/Nu/Sub_Nu_1/Extra_Nu_2',
                'Extra_Nu_3':
                'https://example.com/Main_B/Nu/Sub_Nu_1/Extra_Nu_3',
                'Extra_Nu_4':
                'https://example.com/Main_B/Nu/Sub_Nu_1/Extra_Nu_4',
                'Extra_Nu_5':
                'https://example.com/Main_B/Nu/Sub_Nu_1/Extra_Nu_5'
            },
            'Sub_Nu_2': {  # Подподдиректория
                'Extra_Nu_6':
                'https://example.com/Main_B/Nu/Sub_Nu_2/Extra_Nu_6',
                'Extra_Nu_7':
                'https://example.com/Main_B/Nu/Sub_Nu_2/Extra_Nu_7',
                'Extra_Nu_8':
                'https://example.com/Main_B/Nu/Sub_Nu_2/Extra_Nu_8',
                'Extra_Nu_9':
                'https://example.com/Main_B/Nu/Sub_Nu_2/Extra_Nu_9',
                'Extra_Nu_10':
                'https://example.com/Main_B/Nu/Sub_Nu_2/Extra_Nu_10'
            },
            'Sub_Nu_3': {  # Подподдиректория
                'Extra_Nu_11':
                'https://example.com/Main_B/Nu/Sub_Nu_3/Extra_Nu_11',
                'Extra_Nu_12':
                'https://example.com/Main_B/Nu/Sub_Nu_3/Extra_Nu_12',
                'Extra_Nu_13':
                'https://example.com/Main_B/Nu/Sub_Nu_3/Extra_Nu_13',
                'Extra_Nu_14':
                'https://example.com/Main_B/Nu/Sub_Nu_3/Extra_Nu_14',
                'Extra_Nu_15':
                'https://example.com/Main_B/Nu/Sub_Nu_3/Extra_Nu_15'
            },
            'Sub_Nu_4': {  # Подподдиректория
                'Extra_Nu_16':
                'https://example.com/Main_B/Nu/Sub_Nu_4/Extra_Nu_16',
                'Extra_Nu_17':
                'https://example.com/Main_B/Nu/Sub_Nu_4/Extra_Nu_17',
                'Extra_Nu_18':
                'https://example.com/Main_B/Nu/Sub_Nu_4/Extra_Nu_18',
                'Extra_Nu_19':
                'https://example.com/Main_B/Nu/Sub_Nu_4/Extra_Nu_19',
                'Extra_Nu_20':
                'https://example.com/Main_B/Nu/Sub_Nu_4/Extra_Nu_20'
            },
            'Sub_Nu_5': {  # Подподдиректория
                'Extra_Nu_21':
                'https://example.com/Main_B/Nu/Sub_Nu_5/Extra_Nu_21',
                'Extra_Nu_22':
                'https://example.com/Main_B/Nu/Sub_Nu_5/Extra_Nu_22',
                'Extra_Nu_23':
                'https://example.com/Main_B/Nu/Sub_Nu_5/Extra_Nu_23',
                'Extra_Nu_24':
                'https://example.com/Main_B/Nu/Sub_Nu_5/Extra_Nu_24',
                'Extra_Nu_25':
                'https://example.com/Main_B/Nu/Sub_Nu_5/Extra_Nu_25'
            }
        },
        'Xi': {  # Поддиректория
            'Sub_Xi_1': {  # Подподдиректория
                'Extra_Xi_1':
                'https://example.com/Main_B/Xi/Sub_Xi_1/Extra_Xi_1',
                'Extra_Xi_2':
                'https://example.com/Main_B/Xi/Sub_Xi_1/Extra_Xi_2',
                'Extra_Xi_3':
                'https://example.com/Main_B/Xi/Sub_Xi_1/Extra_Xi_3',
                'Extra_Xi_4':
                'https://example.com/Main_B/Xi/Sub_Xi_1/Extra_Xi_4',
                'Extra_Xi_5':
                'https://example.com/Main_B/Xi/Sub_Xi_1/Extra_Xi_5'
            },
            'Sub_Xi_2': {  # Подподдиректория
                'Extra_Xi_6':
                'https://example.com/Main_B/Xi/Sub_Xi_2/Extra_Xi_6',
                'Extra_Xi_7':
                'https://example.com/Main_B/Xi/Sub_Xi_2/Extra_Xi_7',
                'Extra_Xi_8':
                'https://example.com/Main_B/Xi/Sub_Xi_2/Extra_Xi_8',
                'Extra_Xi_9':
                'https://example.com/Main_B/Xi/Sub_Xi_2/Extra_Xi_9',
                'Extra_Xi_10':
                'https://example.com/Main_B/Xi/Sub_Xi_2/Extra_Xi_10'
            },
            'Sub_Xi_3': {  # Подподдиректория
                'Extra_Xi_11':
                'https://example.com/Main_B/Xi/Sub_Xi_3/Extra_Xi_11',
                'Extra_Xi_12':
                'https://example.com/Main_B/Xi/Sub_Xi_3/Extra_Xi_12',
                'Extra_Xi_13':
                'https://example.com/Main_B/Xi/Sub_Xi_3/Extra_Xi_13',
                'Extra_Xi_14':
                'https://example.com/Main_B/Xi/Sub_Xi_3/Extra_Xi_14',
                'Extra_Xi_15':
                'https://example.com/Main_B/Xi/Sub_Xi_3/Extra_Xi_15'
            },
            'Sub_Xi_4': {  # Подподдиректория
                'Extra_Xi_16':
                'https://example.com/Main_B/Xi/Sub_Xi_4/Extra_Xi_16',
                'Extra_Xi_17':
                'https://example.com/Main_B/Xi/Sub_Xi_4/Extra_Xi_17',
                'Extra_Xi_18':
                'https://example.com/Main_B/Xi/Sub_Xi_4/Extra_Xi_18',
                'Extra_Xi_19':
                'https://example.com/Main_B/Xi/Sub_Xi_4/Extra_Xi_19',
                'Extra_Xi_20':
                'https://example.com/Main_B/Xi/Sub_Xi_4/Extra_Xi_20'
            },
            'Sub_Xi_5': {  # Подподдиректория
                'Extra_Xi_21':
                'https://example.com/Main_B/Xi/Sub_Xi_5/Extra_Xi_21',
                'Extra_Xi_22':
                'https://example.com/Main_B/Xi/Sub_Xi_5/Extra_Xi_22',
                'Extra_Xi_23':
                'https://example.com/Main_B/Xi/Sub_Xi_5/Extra_Xi_23',
                'Extra_Xi_24':
                'https://example.com/Main_B/Xi/Sub_Xi_5/Extra_Xi_24',
                'Extra_Xi_25':
                'https://example.com/Main_B/Xi/Sub_Xi_5/Extra_Xi_25'
            }
        },
        'Omicron': {  # Поддиректория
            'Sub_Omicron_1': {  # Подподдиректория
                'Extra_Omicron_1':
                'https://example.com/Main_B/Omicron/Sub_Omicron_1/Extra_Omicron_1',
                'Extra_Omicron_2':
                'https://example.com/Main_B/Omicron/Sub_Omicron_1/Extra_Omicron_2',
                'Extra_Omicron_3':
                'https://example.com/Main_B/Omicron/Sub_Omicron_1/Extra_Omicron_3',
                'Extra_Omicron_4':
                'https://example.com/Main_B/Omicron/Sub_Omicron_1/Extra_Omicron_4',
                'Extra_Omicron_5':
                'https://example.com/Main_B/Omicron/Sub_Omicron_1/Extra_Omicron_5'
            },
            'Sub_Omicron_2': {  # Подподдиректория
                'Extra_Omicron_6':
                'https://example.com/Main_B/Omicron/Sub_Omicron_2/Extra_Omicron_6',
                'Extra_Omicron_7':
                'https://example.com/Main_B/Omicron/Sub_Omicron_2/Extra_Omicron_7',
                'Extra_Omicron_8':
                'https://example.com/Main_B/Omicron/Sub_Omicron_2/Extra_Omicron_8',
                'Extra_Omicron_9':
                'https://example.com/Main_B/Omicron/Sub_Omicron_2/Extra_Omicron_9',
                'Extra_Omicron_10':
                'https://example.com/Main_B/Omicron/Sub_Omicron_2/Extra_Omicron_10'
            },
            'Sub_Omicron_3': {  # Подподдиректория
                'Extra_Omicron_11':
                'https://example.com/Main_B/Omicron/Sub_Omicron_3/Extra_Omicron_11',
                'Extra_Omicron_12':
                'https://example.com/Main_B/Omicron/Sub_Omicron_3/Extra_Omicron_12',
                'Extra_Omicron_13':
                'https://example.com/Main_B/Omicron/Sub_Omicron_3/Extra_Omicron_13',
                'Extra_Omicron_14':
                'https://example.com/Main_B/Omicron/Sub_Omicron_3/Extra_Omicron_14',
                'Extra_Omicron_15':
                'https://example.com/Main_B/Omicron/Sub_Omicron_3/Extra_Omicron_15'
            },
            'Sub_Omicron_4': {  # Подподдиректория
                'Extra_Omicron_16':
                'https://example.com/Main_B/Omicron/Sub_Omicron_4/Extra_Omicron_16',
                'Extra_Omicron_17':
                'https://example.com/Main_B/Omicron/Sub_Omicron_4/Extra_Omicron_17',
                'Extra_Omicron_18':
                'https://example.com/Main_B/Omicron/Sub_Omicron_4/Extra_Omicron_18',
                'Extra_Omicron_19':
                'https://example.com/Main_B/Omicron/Sub_Omicron_4/Extra_Omicron_19',
                'Extra_Omicron_20':
                'https://example.com/Main_B/Omicron/Sub_Omicron_4/Extra_Omicron_20'
            },
            'Sub_Omicron_5': {  # Подподдиректория
                'Extra_Omicron_21':
                'https://example.com/Main_B/Omicron/Sub_Omicron_5/Extra_Omicron_21',
                'Extra_Omicron_22':
                'https://example.com/Main_B/Omicron/Sub_Omicron_5/Extra_Omicron_22',
                'Extra_Omicron_23':
                'https://example.com/Main_B/Omicron/Sub_Omicron_5/Extra_Omicron_23',
                'Extra_Omicron_24':
                'https://example.com/Main_B/Omicron/Sub_Omicron_5/Extra_Omicron_24',
                'Extra_Omicron_25':
                'https://example.com/Main_B/Omicron/Sub_Omicron_5/Extra_Omicron_25'
            }
        },
        'Pi': {  # Поддиректория
            'Sub_Pi_1': {  # Подподдиректория
                'Extra_Pi_1':
                'https://example.com/Main_B/Pi/Sub_Pi_1/Extra_Pi_1',
                'Extra_Pi_2':
                'https://example.com/Main_B/Pi/Sub_Pi_1/Extra_Pi_2',
                'Extra_Pi_3':
                'https://example.com/Main_B/Pi/Sub_Pi_1/Extra_Pi_3',
                'Extra_Pi_4':
                'https://example.com/Main_B/Pi/Sub_Pi_1/Extra_Pi_4',
                'Extra_Pi_5':
                'https://example.com/Main_B/Pi/Sub_Pi_1/Extra_Pi_5'
            },
            'Sub_Pi_2': {  # Подподдиректория
                'Extra_Pi_6':
                'https://example.com/Main_B/Pi/Sub_Pi_2/Extra_Pi_6',
                'Extra_Pi_7':
                'https://example.com/Main_B/Pi/Sub_Pi_2/Extra_Pi_7',
                'Extra_Pi_8':
                'https://example.com/Main_B/Pi/Sub_Pi_2/Extra_Pi_8',
                'Extra_Pi_9':
                'https://example.com/Main_B/Pi/Sub_Pi_2/Extra_Pi_9',
                'Extra_Pi_10':
                'https://example.com/Main_B/Pi/Sub_Pi_2/Extra_Pi_10'
            },
            'Sub_Pi_3': {  # Подподдиректория
                'Extra_Pi_11':
                'https://example.com/Main_B/Pi/Sub_Pi_3/Extra_Pi_11',
                'Extra_Pi_12':
                'https://example.com/Main_B/Pi/Sub_Pi_3/Extra_Pi_12',
                'Extra_Pi_13':
                'https://example.com/Main_B/Pi/Sub_Pi_3/Extra_Pi_13',
                'Extra_Pi_14':
                'https://example.com/Main_B/Pi/Sub_Pi_3/Extra_Pi_14',
                'Extra_Pi_15':
                'https://example.com/Main_B/Pi/Sub_Pi_3/Extra_Pi_15'
            },
            'Sub_Pi_4': {  # Подподдиректория
                'Extra_Pi_16':
                'https://example.com/Main_B/Pi/Sub_Pi_4/Extra_Pi_16',
                'Extra_Pi_17':
                'https://example.com/Main_B/Pi/Sub_Pi_4/Extra_Pi_17',
                'Extra_Pi_18':
                'https://example.com/Main_B/Pi/Sub_Pi_4/Extra_Pi_18',
                'Extra_Pi_19':
                'https://example.com/Main_B/Pi/Sub_Pi_4/Extra_Pi_19',
                'Extra_Pi_20':
                'https://example.com/Main_B/Pi/Sub_Pi_4/Extra_Pi_20'
            },
            'Sub_Pi_5': {  # Подподдиректория
                'Extra_Pi_21':
                'https://example.com/Main_B/Pi/Sub_Pi_5/Extra_Pi_21',
                'Extra_Pi_22':
                'https://example.com/Main_B/Pi/Sub_Pi_5/Extra_Pi_22',
                'Extra_Pi_23':
                'https://example.com/Main_B/Pi/Sub_Pi_5/Extra_Pi_23',
                'Extra_Pi_24':
                'https://example.com/Main_B/Pi/Sub_Pi_5/Extra_Pi_24',
                'Extra_Pi_25':
                'https://example.com/Main_B/Pi/Sub_Pi_5/Extra_Pi_25'
            }
        },
        'Rho': {  # Поддиректория
            'Sub_Rho_1': {  # Подподдиректория
                'Extra_Rho_1':
                'https://example.com/Main_B/Rho/Sub_Rho_1/Extra_Rho_1',
                'Extra_Rho_2':
                'https://example.com/Main_B/Rho/Sub_Rho_1/Extra_Rho_2',
                'Extra_Rho_3':
                'https://example.com/Main_B/Rho/Sub_Rho_1/Extra_Rho_3',
                'Extra_Rho_4':
                'https://example.com/Main_B/Rho/Sub_Rho_1/Extra_Rho_4',
                'Extra_Rho_5':
                'https://example.com/Main_B/Rho/Sub_Rho_1/Extra_Rho_5'
            },
            'Sub_Rho_2': {  # Подподдиректория
                'Extra_Rho_6':
                'https://example.com/Main_B/Rho/Sub_Rho_2/Extra_Rho_6',
                'Extra_Rho_7':
                'https://example.com/Main_B/Rho/Sub_Rho_2/Extra_Rho_7',
                'Extra_Rho_8':
                'https://example.com/Main_B/Rho/Sub_Rho_2/Extra_Rho_8',
                'Extra_Rho_9':
                'https://example.com/Main_B/Rho/Sub_Rho_2/Extra_Rho_9',
                'Extra_Rho_10':
                'https://example.com/Main_B/Rho/Sub_Rho_2/Extra_Rho_10'
            },
            'Sub_Rho_3': {  # Подподдиректория
                'Extra_Rho_11':
                'https://example.com/Main_B/Rho/Sub_Rho_3/Extra_Rho_11',
                'Extra_Rho_12':
                'https://example.com/Main_B/Rho/Sub_Rho_3/Extra_Rho_12',
                'Extra_Rho_13':
                'https://example.com/Main_B/Rho/Sub_Rho_3/Extra_Rho_13',
                'Extra_Rho_14':
                'https://example.com/Main_B/Rho/Sub_Rho_3/Extra_Rho_14',
                'Extra_Rho_15':
                'https://example.com/Main_B/Rho/Sub_Rho_3/Extra_Rho_15'
            },
            'Sub_Rho_4': {  # Подподдиректория
                'Extra_Rho_16':
                'https://example.com/Main_B/Rho/Sub_Rho_4/Extra_Rho_16',
                'Extra_Rho_17':
                'https://example.com/Main_B/Rho/Sub_Rho_4/Extra_Rho_17',
                'Extra_Rho_18':
                'https://example.com/Main_B/Rho/Sub_Rho_4/Extra_Rho_18',
                'Extra_Rho_19':
                'https://example.com/Main_B/Rho/Sub_Rho_4/Extra_Rho_19',
                'Extra_Rho_20':
                'https://example.com/Main_B/Rho/Sub_Rho_4/Extra_Rho_20'
            },
            'Sub_Rho_5': {  # Подподдиректория
                'Extra_Rho_21':
                'https://example.com/Main_B/Rho/Sub_Rho_5/Extra_Rho_21',
                'Extra_Rho_22':
                'https://example.com/Main_B/Rho/Sub_Rho_5/Extra_Rho_22',
                'Extra_Rho_23':
                'https://example.com/Main_B/Rho/Sub_Rho_5/Extra_Rho_23',
                'Extra_Rho_24':
                'https://example.com/Main_B/Rho/Sub_Rho_5/Extra_Rho_24',
                'Extra_Rho_25':
                'https://example.com/Main_B/Rho/Sub_Rho_5/Extra_Rho_25'
            }
        },
        'Sigma': {  # Поддиректория
            'Sub_Sigma_1': {  # Подподдиректория
                'Extra_Sigma_1':
                'https://example.com/Main_B/Sigma/Sub_Sigma_1/Extra_Sigma_1',
                'Extra_Sigma_2':
                'https://example.com/Main_B/Sigma/Sub_Sigma_1/Extra_Sigma_2',
                'Extra_Sigma_3':
                'https://example.com/Main_B/Sigma/Sub_Sigma_1/Extra_Sigma_3',
                'Extra_Sigma_4':
                'https://example.com/Main_B/Sigma/Sub_Sigma_1/Extra_Sigma_4',
                'Extra_Sigma_5':
                'https://example.com/Main_B/Sigma/Sub_Sigma_1/Extra_Sigma_5'
            },
            'Sub_Sigma_2': {  # Подподдиректория
                'Extra_Sigma_6':
                'https://example.com/Main_B/Sigma/Sub_Sigma_2/Extra_Sigma_6',
                'Extra_Sigma_7':
                'https://example.com/Main_B/Sigma/Sub_Sigma_2/Extra_Sigma_7',
                'Extra_Sigma_8':
                'https://example.com/Main_B/Sigma/Sub_Sigma_2/Extra_Sigma_8',
                'Extra_Sigma_9':
                'https://example.com/Main_B/Sigma/Sub_Sigma_2/Extra_Sigma_9',
                'Extra_Sigma_10':
                'https://example.com/Main_B/Sigma/Sub_Sigma_2/Extra_Sigma_10'
            },
            'Sub_Sigma_3': {  # Подподдиректория
                'Extra_Sigma_11':
                'https://example.com/Main_B/Sigma/Sub_Sigma_3/Extra_Sigma_11',
                'Extra_Sigma_12':
                'https://example.com/Main_B/Sigma/Sub_Sigma_3/Extra_Sigma_12',
                'Extra_Sigma_13':
                'https://example.com/Main_B/Sigma/Sub_Sigma_3/Extra_Sigma_13',
                'Extra_Sigma_14':
                'https://example.com/Main_B/Sigma/Sub_Sigma_3/Extra_Sigma_14',
                'Extra_Sigma_15':
                'https://example.com/Main_B/Sigma/Sub_Sigma_3/Extra_Sigma_15'
            },
            'Sub_Sigma_4': {  # Подподдиректория
                'Extra_Sigma_16':
                'https://example.com/Main_B/Sigma/Sub_Sigma_4/Extra_Sigma_16',
                'Extra_Sigma_17':
                'https://example.com/Main_B/Sigma/Sub_Sigma_4/Extra_Sigma_17',
                'Extra_Sigma_18':
                'https://example.com/Main_B/Sigma/Sub_Sigma_4/Extra_Sigma_18',
                'Extra_Sigma_19':
                'https://example.com/Main_B/Sigma/Sub_Sigma_4/Extra_Sigma_19',
                'Extra_Sigma_20':
                'https://example.com/Main_B/Sigma/Sub_Sigma_4/Extra_Sigma_20'
            },
            'Sub_Sigma_5': {  # Подподдиректория
                'Extra_Sigma_21':
                'https://example.com/Main_B/Sigma/Sub_Sigma_5/Extra_Sigma_21',
                'Extra_Sigma_22':
                'https://example.com/Main_B/Sigma/Sub_Sigma_5/Extra_Sigma_22',
                'Extra_Sigma_23':
                'https://example.com/Main_B/Sigma/Sub_Sigma_5/Extra_Sigma_23',
                'Extra_Sigma_24':
                'https://example.com/Main_B/Sigma/Sub_Sigma_5/Extra_Sigma_24',
                'Extra_Sigma_25':
                'https://example.com/Main_B/Sigma/Sub_Sigma_5/Extra_Sigma_25'
            }
        }
    }
}


# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = []
    for main_dir in PRODUCTS:
        keyboard.append([
            InlineKeyboardButton(f"📂 {main_dir}",
                                 callback_data=f"main_dir:{main_dir}")
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите основную директорию:',
                                    reply_markup=reply_markup)


# Обработчик нажатий на кнопки
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data.split(':')
    action = data[0]
    value = ':'.join(
        data[1:]
    )  # Если значение содержит символ ":" (например, "Main_A:Alpha")

    if action == "main_dir":
        # Показываем поддиректории выбранной основной директории
        main_dir = value
        keyboard = []
        for sub_dir in PRODUCTS[main_dir]:
            keyboard.append([
                InlineKeyboardButton(
                    f"📁 {sub_dir}",
                    callback_data=f"sub_dir:{main_dir}:{sub_dir}")
            ])
        keyboard.append(
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"Выберите поддиректорию в {main_dir}:",
            reply_markup=reply_markup)

    elif action == "sub_dir":
        # Показываем подподдиректории выбранной поддиректории
        main_dir, sub_dir = value.split(':')
        keyboard = []
        for sub_sub_dir in PRODUCTS[main_dir][sub_dir]:
            if isinstance(PRODUCTS[main_dir][sub_dir][sub_sub_dir], dict):
                # Если это словарь (дополнительные директории), показываем кнопку для перехода
                keyboard.append([
                    InlineKeyboardButton(
                        f"📦 {sub_sub_dir}",
                        callback_data=
                        f"sub_sub_dir:{main_dir}:{sub_dir}:{sub_sub_dir}")
                ])
            else:
                # Иначе показываем обычную подподдиректорию
                keyboard.append([
                    InlineKeyboardButton(
                        f"📦 {sub_sub_dir}",
                        callback_data=
                        f"product:{main_dir}:{sub_dir}:{sub_sub_dir}")
                ])
        keyboard.append([
            InlineKeyboardButton("⬅️ Назад",
                                 callback_data=f"main_dir:{main_dir}")
        ])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"Выберите подподдиректорию в {sub_dir}:",
            reply_markup=reply_markup)

    elif action == "sub_sub_dir":
        # Показываем дополнительные директории внутри подподдиректории
        main_dir, sub_dir, sub_sub_dir = value.split(':')
        keyboard = []
        for additional_dir in PRODUCTS[main_dir][sub_dir][sub_sub_dir]:
            product_link = PRODUCTS[main_dir][sub_dir][sub_sub_dir][
                additional_dir]
            keyboard.append([
                InlineKeyboardButton(
                    f"📦 {additional_dir}",
                    callback_data=
                    f"product:{main_dir}:{sub_dir}:{sub_sub_dir}:{additional_dir}"
                )
            ])
        keyboard.append([
            InlineKeyboardButton("⬅️ Назад",
                                 callback_data=f"sub_dir:{main_dir}:{sub_dir}")
        ])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"Выберите дополнительную директорию в {sub_sub_dir}:",
            reply_markup=reply_markup)

    elif action == "product":
        # Показываем ссылку на товар
        main_dir, sub_dir, sub_sub_dir, *additional_dir = value.split(':')
        additional_dir = ':'.join(additional_dir) if additional_dir else None
        if additional_dir:
            product_link = PRODUCTS[main_dir][sub_dir][sub_sub_dir][
                additional_dir]
        else:
            product_link = PRODUCTS[main_dir][sub_dir][sub_sub_dir]
        keyboard = [[
            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data=f"sub_sub_dir:{main_dir}:{sub_dir}:{sub_sub_dir}"
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=
            f"Вы выбрали {main_dir} - {sub_dir} - {sub_sub_dir} - {additional_dir}. Ссылка: {product_link}",
            reply_markup=reply_markup)

    elif action == "back_to_main":
        # Возвращаемся к выбору основной директории
        keyboard = []
        for main_dir in PRODUCTS:
            keyboard.append([
                InlineKeyboardButton(f"📂 {main_dir}",
                                     callback_data=f"main_dir:{main_dir}")
            ])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите основную директорию:",
                                      reply_markup=reply_markup)


# Основная функция
def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
