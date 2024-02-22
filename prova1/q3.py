class ConversaoDeUnidadesDeTempo:
    def __init__(self, tempo, unidade):
        self.tempo = tempo
        self.unidade = unidade

    def para_segundos(self):
        if(self.unidade == 'minuto'):
            return self.tempo * 60
        if(self.unidade == 'hora'):
            return self.tempo * 3600
        if(self.unidade == 'dia'):
            return self.tempo * 86400
        if(self.unidade == 'semana'):
            return self.tempo * (86400 * 7)
        if(self.tempo == 'mes'):
            return self.tempo * (86400 * 30)

    def para_minutos(self):
        valor = self.para_segundos()
        return valor / 60
    
    def para_horas(self):
        valor = self.para_segundos()
        return valor / 3600
    
    def para_dias(self):
        valor = self.para_segundos()
        return valor / 86400
    
    def para_semanas(self):
        valor = self.para_dias()
        return valor / 7
    
    def para_meses(self):
        valor = self.para_dias()
        return valor / 30
    
conversor = ConversaoDeUnidadesDeTempo(7, 'dia')

print(conversor.para_semanas())