casa = {

    "hall": {
        "liga": ["sala", "cozinha", "corredor"]
    },

    "sala": {
        "liga": ["hall"],
        "obstaculos": [
            "sofa",
            "mesa",
            "movel_tv"
        ]
    },

    "cozinha": {
        "liga": ["hall"],
        "obstaculos": [
            "bancada",
            "mesa",
            "frigorifico"
        ]
    },

    "corredor": {
        "liga": [
            "hall",
            "quarto1",
            "quarto2"
        ]
    },

    "quarto1": {
        "liga": [
            "corredor",
            "casa_banho1"
        ],
        "obstaculos": [
            "cama",
            "secretaria"
        ]
    },

    "quarto2": {
        "liga": [
            "corredor",
            "casa_banho2"
        ],
        "obstaculos": [
            "cama"
        ]
    },

    "casa_banho1": {
        "liga": [
            "quarto1"
        ],
        "obstaculos": [
            "lavatorio",
            "sanita"
        ]
    },

    "casa_banho2": {
        "liga": [
            "quarto2"
        ],
        "obstaculos": [
            "lavatorio",
            "sanita"
        ]
    }

}