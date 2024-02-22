class Continente {
    constructor(continente) {
        this.continente = continente
    }

    paises = []

    adicionarPais(pais, continente, dimensao, populacao) {
        this.paises.push({
            pais,
            continente,
            dimensao,
            populacao
        })
    }

    getDimensaoTotal() {
        let soma = 0

        for(let i = 0; i < this.paises.length; i++) {
            soma += this.paises[i].dimensao
        }

        return soma
    }

    getPopulacaoTotal() {
        let soma = 0

        for(let i = 0; i < this.paises.length; i++) {
            soma += this.paises[i].populacao
        }

        return soma
    }

    getDensidadePopulacional() {
        const populacao = this.getPopulacaoTotal()
        const dimensao = this.getDimensaoTotal()

        return dimensao / populacao
    }

    getPaisComMaiorPopulacao() {
        let maiorPopulacao = 0

        for(let i = 0; i < this.paises.length; i++) {
            if (this.paises[i].populacao > maiorPopulacao) {
                maiorPopulacao = i
            }
        }

        return this.paises[maiorPopulacao]
    }

    getPaismenorPopulacao() {
        let menorPopulacao

        for(let i = 0; i < this.paises.length; i++) {
            menorPopulacao = this.paises[i].populacao
            if (this.paises[i].populacao < menorPopulacao) {
                menorPopulacao = i
            }
        }

        return this.paises[menorPopulacao]
    }

    getPaisMaiorDimensao() {
        let maiorDimensao = 0

        for(let i = 0; i < this.paises.length; i++) {
            if (this.paises[i].dimensao < maiorDimensao) {
                maiorDimensao = i
            }
        }

        return this.paises[maiorDimensao]
    }

    getPaisMenorDimensao() {
        let menorDimensao
        let indicePais = 0

        for(let i = 0; i < this.paises.length; i++) {
            menorDimensao = this.paises[i].dimensao
            if (this.paises[i].dimensao > menorDimensao) {
                menorDimensao = this.paises[i].dimensao
                indicePais = i
            }
        }

        return this.paises[indicePais]
    }
}

const americaDoSul = new Continente('América do Sul')

americaDoSul.adicionarPais('BRA', 'América do Sul', 500, 10)
americaDoSul.adicionarPais('ARG', 'América do Sul', 200, 5)
americaDoSul.adicionarPais('PER', 'América do Sul', 300, 12)

console.log(americaDoSul.paises)