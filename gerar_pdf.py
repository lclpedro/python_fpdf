from fpdf import FPDF
@app.route('/api/projeto/gerarpdf/<cod_projeto>', methods=['GET'])
def gerarPdfProjeto(cod_projeto):
	class PDF(FPDF):
		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','I', 8)
			self.multi_cell(0,10,'Página'+str(self.page_no())+'/{nb}',0,0,'L')
	pdf = PDF()
	pdf.alias_nb_pages()
	pdf.add_page()
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(0,5,'CARTA CONSULTA', align='C')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(0,10,'__nome da cidade/estado__ de ___mes___ de ___ano__', align='R')
	pdf.ln(8)
	pdf.ln(3)
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180, 5, 'Ao senhor \nNOME DO PRESIDENTE DA COMISSÃO \nPresidente da Comissão da Política de Incentivos às Atividades Industriais do Estado do Acre - COPIAI/AC',align='L')
	pdf.ln(25)
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(190, 5, '        Prezado Senhor,',align='L')
	pdf.multi_cell(190, 5, '        Através da presente, ___(Nome do sócio/proprietário ou representante legal), representante legal da empresa ___(nome da empresa)__, empresenta para fins \
		de análise, consulta para obtenção dos incentivos previstos na(s) Lei(s) nº _____ e/ou ____.', align='L')
	pdf.multi_cell(190, 5, '        Para efeito de melhor análise do pleito, anexa dados sobre empreendimento e declara-se conhecedor das normas legais e administrativas pertinentes ao assunto.',align='L')
	pdf.ln(10)
	pdf.multi_cell(190, 5, '        Atenciosamente,',align='L')
	pdf.ln(10)
	pdf.multi_cell(190, 5, '___________________________________________',align='C')
	pdf.multi_cell(190, 5, '(Carimbo e assinatura do representante legal)',align='C')
	pdf.set_font('Arial', 'B', 12)
	pdf.add_page()

	pdf.multi_cell(180, 5, '\n1. IDENTIFICAÇÃO DO REPRESENTANTE LEGAL',align='L')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'Nome Completo:',1,1,'L',0)
	pdf.cell(90,5,'CPF:',1,0,'L',0)
	pdf.cell(90,5,'RG:',1,1,'L',0)
	pdf.cell(90,5,'Endereço:',1,0,'L',0)
	pdf.cell(90,5,'Bairro:',1,1,'L',0)
	pdf.cell(80,5,'Cidade:',1,0,'L',0)
	pdf.cell(40,5,'UF:',1,0,'L',0)
	pdf.cell(60,5,'CEP:',1,1,'L',0)
	pdf.cell(60,5,'Telefone:',1,0,'L',0)
	pdf.cell(60,5,'Celular:',1,0,'L',0)
	pdf.cell(60,5,'Fax:',1,1,'L',0)
	pdf.cell(180,5,'E-mail:',1,0,'L',0)
	pdf.ln(5)
	pdf.set_font('Arial', 'B', 12)

	pdf.multi_cell(180, 5, '\n2. IDENTIFICAÇÃO DA EMPRESA',align='L')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'Razão Social:',1,0, 'L', 0)
	pdf.multi_cell(180,5,'Nome Fantasia:',1,0, 'L', 0)
	pdf.cell(60,5,'CNPJ', 1,0,'L',0)
	pdf.cell(60,5,'Incrição Estadual:', 1,0,'L',0)
	pdf.cell(60,5,'Data de Constituição:', 1,1,'L',0)
	pdf.cell(90,5,'Forma Jurídica:', 1,0,'L',0)
	pdf.cell(90,5,'Regime Tributário:', 1,1,'L',0)
	pdf.cell(120,5,'Endereço:', 1,0,'L',0)
	pdf.cell(60,5,'Bairro:', 1,1,'L',0)
	pdf.cell(80,5,'Cidade:',1,0,'L',0)
	pdf.cell(40,5,'UF:',1,0,'L',0)
	pdf.cell(60,5,'CEP:',1,1,'L',0)
	pdf.cell(60,5,'Telefone:',1,0,'L',0)
	pdf.cell(60,5,'Ramal:',1,0,'L',0)
	pdf.cell(60,5,'Fax:',1,1,'L',0)
	pdf.multi_cell(180,5,'Email Corporativo:',1,0,'L',0)
	pdf.multi_cell(180,5,'Site:',1,0,'L',0)
	pdf.multi_cell(180,5,'Atividade Econômica Principal (Industrial)',1,0,'L',0)
	pdf.multi_cell(180,5,'Atividades Econômicas Secundárias:',1,0,'L',0)
	# for und in atividades Secundárias:
		# pdf.multi_cell(180,5,'-Atividade 1',1,0,'L',0)
	pdf.multi_cell(180,5,'Capital Social da Empresa:',1,0,'L',0)
	pdf.cell(80,5,'Sócio:',1,0,'L',0)
	pdf.cell(35,5,'Participação (%):',1,0,'L',0)
	pdf.cell(35,5,'Nº de Quotas:',1,0,'L',0)
	pdf.cell(30,5,'Valor (R$):',1,1,'L',0)
	# for und in socios:
	pdf.cell(80,5,'Pedro Lucas Costa Lima',1,0,'L',0)
	pdf.cell(35,5,'100%',1,0,'L',0)
	pdf.cell(35,5,'1500',1,0,'L',0)
	pdf.cell(30,5,'R$ 300.000,00',1,1,'L',0)
	pdf.multi_cell(180,5,'Organização Administrativa:',1,0,'L',0)
	pdf.ln(5)
	pdf.set_font('Arial', 'B', 12)

	pdf.multi_cell(180, 5, '\n3. INFORMAÇÕES SOBRE O NEGÓCIO',align='L')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'Missão da Empresa:',1,0,'L',0)
	pdf.multi_cell(180,5,'Objetivos e Metas da Empresa:',1,0,'L',0)
	#for und in objetivos_empresa
	pdf.multi_cell(180,5,'Descrição da Empresa:',1,0,'L',0)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'PROCESSO PRODUTIVO',1,0,'L',0)
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'Descrição de Produtos:',1,0,'L',0)
	#for und in produtos
	pdf.multi_cell(180,5,'Descrição do Processo Produtivo E Tecnologia Empregada:',1,0,'L',0)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'CAPACIDADE PRODUTIVA INSTALADA (Qtde./Mês)',1,0,'C',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(90,5,'Na Fase de Implantação:',1,0,'L',0)
	pdf.cell(90,5,'Na Fase de Operação:',1,1,'L',0)
	pdf.ln(3)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'INSUMOS:',1,0,'C',0)
	pdf.multi_cell(180,5,'ORIGEM DA MATÉRIA-PRIMA (Citar as Principais)',1,0,'C',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(90,5,'Discriminação',1,0,'L',0)
	#for und in drisciminacoes
	pdf.cell(90,5,'Origem (Cidade/UF/Pais)',1,1,'L',0)
	pdf.cell(90,5,'-',1,0,'L',0)
	pdf.cell(90,5,'-',1,1,'L',0)
	#for und in origem
	pdf.ln(3)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'VENDAS:',1,0,'L',0)
	pdf.multi_cell(180,5,'Mercado de Potencias (Citar os Principais)',1,0,'C',0)
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'-', 1,0,'L',0)
	#for und in Potencias
	pdf.multi_cell(180,5,'Elementos de diferenciação:', 1,0,'L',0)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'PREVISÃO DE VENDAS (R$)', 1,0,'C')
	pdf.set_font('Arial', '', 12)
	pdf.cell(90,10,'Produtos', 1,0,'C',0)
	pdf.cell(90,5,'Valor Previsto (R$):',1,1,'C',0)
	pdf.cell(90)
	pdf.cell(45,5,'1º Ano:', 1,0,'C',0)
	pdf.cell(45,5,'2º Ano:', 1,1,'C',0)
	pdf.cell(90,5,'-', 1,0,'L',0)
	pdf.cell(45,5,'-', 1,0,'L',0)
	pdf.cell(45,5,'-', 1,1,'L',0)
	pdf.cell(90,5,'Total:', 1,0,'L',0)
	pdf.cell(45,5,'-', 1,0,'L',0)
	pdf.cell(45,5,'-', 1,1,'L',0)
	
	pdf.ln(3)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'RECURSOS HUMANOS:', 1,0,'L',0)
	pdf.multi_cell(180,5,'EMPREGOS DIRETOS GERADOS', 1,0,'L',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(90,5,'Na fase de Implantação', 1,0,'L',0)
	pdf.cell(90,5,'Na fase de Operação', 1,1,'L',0)
	pdf.cell(90,5,'-', 1,0,'L',0)
	pdf.cell(90,5,'-', 1,1,'L',0)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'EMPREGOS DIRETOS GERADOS', 1,0,'L',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(90,5,'Na fase de Implantação', 1,0,'L',0)
	pdf.cell(90,5,'Na fase de Operação', 1,1,'L',0)

	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180, 5, '\n4. ÁREA DEMANDADA (NO CASO DE SOLICITAÇÃO DA LEI 1.359/00)',align='L')
	pdf.set_font('Arial', '', 12)
	pdf.cell(60,5,'Local Pretendido:', 1,0,'L',0)
	pdf.cell(60,5,'Área Total Solicitada (m²)', 1,0,'L',0)
	pdf.cell(60,5,'Área Total a Construir (m²)', 1,1,'L',0)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'PRAZO DA OBRA:',1,0,'L',0)
	pdf.multi_cell(180,5,'PREVISÃO PARA INICIO:',1,0,'L',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(60,5,'Dia: ', 1,0,'L',0)
	pdf.cell(60,5,'Mês: ', 1,0,'L',0)
	pdf.cell(60,5,'Ano: ', 1,1,'L',0)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'PREVISÃO PARA CONCLUSÃO:',1,0,'L',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(60,5,'Dia: ', 1,0,'L',0)
	pdf.cell(60,5,'Mês: ', 1,0,'L',0)
	pdf.cell(60,5,'Ano: ', 1,1,'L',0)

	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180, 5, '\n5. INVESTIMENTOS FIXOS ESTIMADOS (NO CASO DE SOLICITAÇÃO DA LEI 1.358/00)',align='L')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'Valor estimado a ser apresentado (e comprovado com notas fiscais) relativos aos gastos com aquisição de\
		máquinas, equipamentos, instalações e obras de infra-estrutura, inclusive construções, destinadas\
		exclusivamente à produção, excluídos terrenos e veículos de passeio, conforme o Art. 1º, § 1º da Lei\
		1.358/00:',border=1,align='L')
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180, 5, '\n6. DADOS DO PROJETO',align='L')
	pdf.multi_cell(180,5,'FONTES DE RECURSOS PARA A EXECUÇÃO DAS OBRAS (R$ mil)',1,0,'C',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(120,5,'Próprios:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)
	pdf.cell(120,5,'Outros:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)
	pdf.cell(120,5,'Total:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)

	pdf.ln(3)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'INVESTIMENTOS TOTAIS PREVISTOS (R$ mil)',1,0,'C',0)
	pdf.set_font('Arial', '', 12)
	pdf.cell(120,5,'Instalações Físicas:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)
	pdf.cell(120,5,'Equipamentos:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)
	pdf.cell(120,5,'Outros:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)
	pdf.cell(120,5,'Totais:',1,0,'L',0)
	pdf.cell(60,5,'',1,1,'L',0)

	pdf.multi_cell(180, 5, '\n7. OUTRAS INFORMAÇÕES',align='L')
	# pdf.ln(3)
	pdf.multi_cell(180,5,'Previsão de Consumo e Procedência de Energia Elétrica (Kw/mês) - \
		Indicar se pretende gerar energia própria/alternativa, como e a quantidade:',border=1,align='L')
	pdf.ln(3)
	pdf.multi_cell(180,5,'Consumo Previsto de Água (m³):',border=1,align='L')
	pdf.ln(3)
	pdf.multi_cell(180,5,'Previsão de Utilização de Equipamentos ou Processos Antipoluentes que resguardem a proteção do Meio\
		Ambiente (Tratamento ou eliminação de resíduos):',border=1,align='L')
	pdf.ln(3)
	pdf.multi_cell(180,5,'Localização do Empreendimento de Acordo com o Zoneamento Ecológico-Econômico:',border=1,align='L')
	pdf.ln(3)
	pdf.multi_cell(180,5,'Inovações tecnológicas, que priorizem a utilização dos recursos naturais de forma sustentável e o\
		aperfeiçoamento da mão-de- obra local:',border=1,align='L')
	pdf.ln(3)
	pdf.multi_cell(180,5,'Detalhamento da política de treinamento anual de funcionários / Aperfeiçoamento de mão-de- obra da\
		empresa:',border=1,align='L')
	pdf.ln(3)
	pdf.multi_cell(180,5,'Certificados ou Processo/Projeto de Origem de Produção Sustentável:',border=1,align='L')

	pdf.multi_cell(180, 5, '\n8. OUTRAS INFORMAÇÕES',align='L')
	pdf.multi_cell(180,15,' ',border=1,align='L')

	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	
	return pdfgerado

@app.route('/api/processo/capa/<cod_processo>', methods=['GET'])
def impressaoCapaProcesso(cod_processo):
	class PDF(FPDF):
		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','I', 8)
			# self.multi_cell(0,10,'Página'+str(self.page_no())+'/{nb}',0,0,'L')

	pdf = PDF()
	# pdf.alias_nb_pages()
	pdf.add_page()
	pdf.set_font('Arial', 'B', 12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'LOGO \n\
		ESTADO DO ACRE\n\
		Secretaria de Estado de Desenvolvimento da\n\
		Indústria, do Comércio, e dos Serviços Sustentáveis - SEDENS\n\
		Departamento de Política de Incentivos às Atividades\n\
		Industriais do Estado do Acre - COPIAI/AC', border=1, align='C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'PROCESSO:        DATA:        NÚMERO:', border=1, align='C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'INTERESSADO:', border=1, align='C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'ASSUNTO:', border=1, align='C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'ANEXOS:', border=1, align='C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'MOVIMENTO DO PROCESSO', align='C')
	pdf.ln(3)
	pdf.cell(63.3,5,'DE',1,0,'C')
	pdf.cell(63.3,5,'DATA',1,0,'C')
	pdf.cell(63.3,5,'PARA',1,1,'C')
	pdf.cell(63.3,5,'',1,0,'L')
	pdf.cell(21.1,5,'',1,0,'L')
	pdf.cell(21.1,5,'',1,0,'L')
	pdf.cell(21.1,5,'',1,0,'L')
	pdf.cell(63.3,5,'',1,1,'L')
	

	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	
	return pdfgerado

@app.route('/api/documentacao_necessaria/gerarpdf', methods=['GET'])
def impressaoDocNecessario():
	class PDF(FPDF):
		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','I', 8)
			# self.multi_cell(0,10,'Página'+str(self.page_no())+'/{nb}',0,0,'L')

	pdf = PDF()
	# pdf.alias_nb_pages()
	pdf.add_page()
	pdf.ln(5)
	pdf.set_font('Arial', 'B', 16)
	pdf.multi_cell(180,5,'        Para concorrer aos benefícios oferecidos pela COPIAI,\
		a empresa interessada deverá:', align='C')
	pdf.ln(8)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'A) Está consituída no Estado do Acre e efetivamente classificada\
		como Indústria;')
	pdf.multi_cell(180,5,'B) Protocolar na COPIAI Projeto Técnico - Plano de Negócios,\
		contendo os documentos listados abaixo, solicitando enquadramento em uma ou ambas\
		as Leis do Incentivo:')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'        * 1.358/2000 - Financiamento de ICMS;')
	pdf.multi_cell(180,5,'        * 1.358/2000 - Concessão de Áreas;')
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(180,5,'Documentos:')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'     I. Contrato Social e alterações devidamente registrados na JUCEAC - Junta\
		Comercial do Estado do Acre;')
	pdf.multi_cell(180,5,'     II. Cadastro Nacional de Pessoa Jurídica - CNPJ;')
	pdf.multi_cell(180,5,'     III. FAC - Inscrição Estadual;')
	pdf.multi_cell(180,5,'     IV. Certidões Negativas de Débitos Fiscais no âmbito Federal, Estadual e\
		Municipal;')
	pdf.multi_cell(180,5,'     V. Certidões Negativas do Cartório de Protestos e do Cartório Distribuidor;')
	pdf.multi_cell(180,5,'     VI. Alvará de Localização e Funcionamento;')
	pdf.multi_cell(180,5,'     VII. Balanço de Abertura, quando se tratar de empresa com menos de um\
		ano de criação;')
	pdf.multi_cell(180,5,'     VIII. Balanço e Demonstrativo de Resultados do último exercício;')
	pdf.multi_cell(180,5,'     IX. Licença Ambiental fornecida pelo IMAC;')
	pdf.multi_cell(180,5,'     X. Notas Fiscais devidamente registradas na SEFAZ/AC ou Escrituras\
		Públicas, referentes ao imobilizado atual (exceto terrenos e veículos de\
		passeio) (Somente para o benefício da Lei nº 1.358/2000);')
	pdf.multi_cell(180,5,'     XI Demonstrativo de arrecadação mensal - DAM (Últimos 12 meses)\
		para as empresas em funcionamento e em regime normal, ou DASN para\
		optantes do Simples Nacional (Somente para o benefício da Lei nº 1.358/2000)')
	pdf.multi_cell(180,5,'     XII. Projeto Arquitetônico, contendo ART, plantas, memorial descritivo,\
		orçamento e cronograma físico-financeiro da obra a ser realizada\
		(Somente para o benefício da Lei nº 1.359/2000);')
	pdf.multi_cell(180,5,'     XIII. Projeto de Segurança Contra Incêndio e Pânico aprovado pelo Corpo de\
		Bombeiros (Somente para o benefício da Lei nº 1.359/2000).')
	pdf.multi_cell(180,5,'     VIII. Balanço e Demonstrativo de Resultados do último exercício;')
	pdf.set_font('Arial', 'B', 12)
	pdf.ln(3)

	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	
	return pdfgerado

@app.route('/api/requerimento/gerarpdf', methods=['GET'])
def impressaoRequerimento():
	class PDF(FPDF):
		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','I', 8)
			# self.multi_cell(0,10,'Página'+str(self.page_no())+'/{nb}',0,0,'L')
	pdf = PDF()
	# pdf.alias_nb_pages()
	pdf.add_page()
	pdf.ln(5)
	pdf.set_font('Arial', 'B', 14)
	pdf.multi_cell(180,5,'REQUERIMENTO', align='C')
	pdf.set_font('Arial', '', 12)
	pdf.multi_cell(180,5,'(Pleiteando Benefícios)', align='C')
	pdf.ln(10)
	pdf.multi_cell(180,5,'Ao Senhor\n(NOME DO PRESIDENTE DA COMISSÃO)', align='L')
	pdf.multi_cell(180,5,'Presidente da Comissão da Política de Incentivos às Atividades Industriais do\
		Estado do Acre - COPIAI/AC')
	pdf.ln(15)
	pdf.multi_cell(180,5,'       Senhor Presidente,\
		A (NATUREZA JURÍDICA DA EMPRESA E RAZÃO SOCIAL DA\
		EMPRESA), pessoa jurídica de direito privado, inscrita no CNPJ sob o nº\
		(........), com Inscrição Estadual nº (........), e classificada no CNAE sob o nº\
		(........) - (DESCRIÇÃO DA ATIVIDADE ECONÔMICA PRINCIPAL DA\
		EMPRESA), solicita a concessão dos incentivos previstos na(s) Lei(s) n°\
		(1.358/00 - incentivo fiscal, e/ou 1.359/00 - concessão de áreas), cujas\
		caracterizações básicas, apresentamos no (PROJETO TÉCNICO/PLANO DE\
		NEGÓCIOS OU REAVALIAÇÃO) em anexo.')
	pdf.ln(30)
	pdf.multi_cell(180,5,'NESTES TERMOS \nPEDE DEFERIMENTO',align='C')
	
	pdf.ln(30)
	pdf.multi_cell(180,5,'Rio Branco,...........de................................de........',align='R')
	
	pdf.ln(15)
	pdf.multi_cell(180,5,'___________________________________________________\nAssinatura e Carimbo',align='C')
	pdf.ln(30)
	pdf.multi_cell(180,5,'Obs.: O número da Lei e o respectivo artigo deverá ser preenchido de acordo\
		com o benefício requerido.',align='C')

	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	
	return pdfgerado

@app.route('/api/processo/checklist/<cod_processo>', methods=['GET'])
def impressaoCheckList(cod_processo):
	class PDF(FPDF):
		def header(self):
			self.set_font('Arial', '', 9)
			self.multi_cell(190,4,'LOGO \n\
				ESTADO DO ACRE\n\
				Secretaria de Estado de Desenvolvimento da\n\
				Indústria, do Comércio, e dos Serviços Sustentáveis - SEDENS\n\
				Departamento de Política de Incentivos às Atividades\n\
				Industriais do Estado do Acre - COPIAI/AC', align='C')
			self.ln(3)

		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','', 8)
			self.cell(20)
			self.multi_cell(90,4, '    Av. Getúlio Vargas, nº 1782 - Bosque\n\
				Rio Branco-Acre - Brasil - CEP. 69. 900 - 610\n\
				Tel. COPIAI: (68) 3215-2396 / Gabinete: (68) 3223-1281', align='L')
			self.cell(100)
			self.multi_cell(90,4, 'LOGO', align='C')

	pdf = PDF()
	pdf.add_page()
	pdf.ln(3)
	pdf.set_font('Arial', '', 9)
	pdf.set_font('Arial', 'B', 9)
	pdf.multi_cell(190,4,'CHECK-LIST DOCUMENTAL DO PROCESSO',align='C')
	pdf.multi_cell(190,8,'NOME DA EMPRESA:', border=1, align='L')
	pdf.set_font('Arial', '', 9)
	pdf.cell(90,8,'Documentos:',1,0,'L')
	pdf.cell(43,4,'Anexado ao processo',1,0,'L')
	pdf.cell(57,8,'Observações:',1,1,'L')
	pdf.cell(90)
	pdf.set_xy(100,56)
	pdf.cell(21.5,4,'Sim',1,0,'L')
	pdf.cell(21.5,4,'Não',1,1,'L')
	pdf.set_font('Arial', '', 8)
	pdf.cell(90,4,'Projeto Técnico - Econômico - Financeiro (Plano de Negócios).',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Contrato social e alterações devidamente registradas na JUCEAC',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Cadastro Nacional de Pessoa Jurídica - CNPJ',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Inscrição Estadual - FAC',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Certidão Negativa de Débito Federal',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Certidão Negativa de Débito Estadual',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Certidão Negativa de Débito Municipal',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Certidão Negativa do Cartório de Protesto',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,4,'Certidão Negativa do Cartório Distribuidor',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.multi_cell(90,3,'Balanço de Abertura, quando se tratar de empresa com menos de um ano de criação.',1,0,'L')
	pdf.set_xy(100,96)
	pdf.cell(21.5,6,'',1,0,'L')
	pdf.cell(21.5,6,'',1,0,'L')
	pdf.cell(57,6,'',1,1,'L')
	pdf.cell(90,4,'Balanço e demonstrativo de resultado do último exercício',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.cell(21.5,4,'',1,0,'L')
	pdf.multi_cell(57,4,'',1,1,'L')
	pdf.cell(90,18,'Alvará de Localização e Funcionamento',1,0,'L')
	pdf.cell(21.5,18,'',1,0,'L')
	pdf.cell(21.5,18,'',1,0,'L')
	pdf.multi_cell(57,3,'Requerente possui prazo de até sessenta dias\
		após a assinatura do Termo de Acordo/Escritura\
		Pública de Concessão para apresentar o\
		documento, conforme texto do Art. 1º dos\
		Decretos nº 12.360 e 12.361, ambos de 23 de\
		junho de 2005.',1,1,'L')
	pdf.cell(90,18,'Licensa Ambiental do IMAC',1,0,'L')
	pdf.cell(21.5,18,'',1,0,'L')
	pdf.cell(21.5,18,'',1,0,'L')
	pdf.multi_cell(57,3,'Requerente possui prazo de até sessenta dias\
		após a assinatura do Termo de Acordo/Escritura\
		Pública de Concessão para apresentar o\
		documento, conforme texto do Art. 1º dos\
		Decretos nº 12.360 e 12.361, ambos de 23 de\
		junho de 2005.',1,1,'L')
	pdf.multi_cell(90,3,'Demonstrativo de Arrecadação Mensal - DAM (últimos 12 meses) para as\
		empresas em funcionamento e em regime normal, ou DASN para optantes\
		do Simples Nacional.',1,0,'L')
	pdf.set_xy(100,142)
	pdf.cell(21.5,9,'',1,0,'L')
	pdf.cell(21.5,9,'',1,0,'L')
	pdf.cell(57,9,'',1,1,'L')
	pdf.multi_cell(90,3,'Notas Fiscais devidamente registradas na SEFAZ/AC ou Escrituras Públicas,\
		referentes ao imobilizado atual (exceto terrenos e veículos de passeio).',1,0,'L')
	pdf.set_xy(100,151)
	pdf.cell(21.5,9,'',1,0,'L')
	pdf.cell(21.5,9,'',1,0,'L')
	pdf.cell(57,9,'',1,1,'L')
	pdf.multi_cell(90,3,'Projeto de Segurança Contra Incêndio e Pânico aprovado pelo Corpo de Bombeiros.',1,0,'L')
	pdf.set_xy(100,160)
	pdf.cell(21.5,6,'',1,0,'L')
	pdf.cell(21.5,6,'',1,0,'L')
	pdf.cell(57,6,'',1,1,'L')
	pdf.multi_cell(90,3,'Projeto Arquitetônico, contendo ART, plantas, memorial descritivo,\
		orçamento e cronograma físico-financeiro da obra a ser realizada.',1,0,'L')
	pdf.set_xy(100,166)
	pdf.cell(21.5,9,'',1,0,'L')
	pdf.cell(21.5,9,'',1,0,'L')
	pdf.cell(57,9,'',1,1,'L')
	pdf.cell(90,8,'Outras informações',1,0,'L')
	pdf.cell(100,8,'',1,1,'L')
	pdf.multi_cell(90,8,'                       Técnico da COPIAI responsável \n \n\
	                     Cliente em: ___/____/________',1,0,'C')
	pdf.set_xy(100,183)
	pdf.multi_cell(100,8,'                      Empresário/Consultor responsável pela Empresa. \n \n\
		                 Cliente em: ___/____/________',1,1,'C')
	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado