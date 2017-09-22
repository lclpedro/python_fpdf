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
	pdf = PDF()
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
	pdf = PDF()
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

@app.route('/api/parecer_tecnico', methods=['GET'])
def parecerTecnico():
	class PDF(FPDF):
		def header(self):
			self.set_font('Arial', '', 9)
			self.multi_cell(190,4,'LOGO \n\
				ESTADO DO ACRE\n\
				Secretaria de Estado de Desenvolvimento da\n\
				Indústria, do Comércio, e dos Serviços Sustentáveis - SEDENS\n', align='C')
			self.ln(3)

		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','', 8)
			self.cell(10)
			self.multi_cell(90,4, '    Av. Getúlio Vargas, nº 1782 - Bosque\n\
				Rio Branco-Acre - Brasil - CEP. 69. 900 - 610\n\
				Tel. COPIAI: (68) 3215-2396 / Gabinete: (68) 3223-1281', align='L')
			self.set_font('Arial','I', 8)
			self.multi_cell(0,10,'Página '+str(self.page_no())+'/{nb}',0,0,'L')
	pdf = PDF()
	pdf.add_page()
	pdf.alias_nb_pages()
	pdf.set_font('Arial', 'B',12)
	pdf.multi_cell(190,5,'PARECER TÉCNICO',align='C')
	pdf.multi_cell(190,5,'PROCESSO: Nº ',align='J')
	pdf.multi_cell(190,5,'ASSUNTO:',align='J')
	pdf.ln(3)
	pdf.multi_cell(190,5,'1 -    DA SOLICITAÇÃO',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        A (natureza jurídica da empresa e razão social da empresa), pessoa jurídica\
		de direito privado, inscrita no CNPJ sob o nº XX.XXX.XXX/XXXX-XX, com Inscrição Estadual nº XX.XXX.XXX/XXX-XX,\
		classificada no CNAE sob o nº XX.XX-X-XX - "(descrição da atividade econômica principal)", apresenta, para fins\
		de análise, Plano de Negócios onde pleiteia a concessão do(s) benefício(s) previsto(s) na(s) Lei(s) n° 1.358/00\
		- regulamentada pelo Decreto nº 4.196 de 1º de outubro de 2001, relativa à concessão de incentivos fiscais na\
		modalidade de financiamento direto ao contribuinte, com até 95% dos saldos devedores de ICMS, conforme nota(s)\
		fiscal(is) apresentada(s) à(s) fl(s). XX dos autos, concernente(s) à aquisição de itens para composição do ativo\
		imobilizado; e/ou na Lei nº 1.359/00 - regulamentada pelo decreto nº 4.197 de 1º de outubro de 2001 -, relativa à\
		concessão de um lote industrial, total de XX.XXX,XX m², localizado no (Parque Industrial/Pólo Moveleiro) de\
		(Município) (fl. XX).',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'2 -    DA ANÁLISE DOCUMENTAL',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        De acordo com o check-list do processo (fl. XXX) e a documentação anexada aos autos, com\
		fundamento no(s) Art. 13º, do Anexo Único do Decreto nº 4.196 de 1º de outubro de 2001 (em caso de solicitação dos\
		incentivos fiscais da Lei 1.358/00), e Art. 2º, Parágrafo Único, do Anexo Único do Decreto Nº 4.197 de 1º de\
		outubro de 2001 (em caso de solicitação dos incentivos fiscais da Lei 1.359/00), atestamos que a requerente apresentou\
		os documentos necessários e exigidos de acordo com a legislação.',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'3 -    DO ENQUADRAMENTO',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        De acordo com as informações constantes no Projeto Técnico/Plano de Negócios, a empresa enquadra-se\
		cumulativamente nos seguintes itens do Art. 4º, do anexo único, de ambos os regulamentos operativos das Leis nº\
		1.358/00 e 1.359/00, respectivamente, Decreto nº 4.196 de 1º de outubro de 2001 e Decreto Nº 4.197 de 1º de\
		outubro de 2001:',align='J')
	pdf.ln(3)
	pdf.multi_cell(190,5,'I.	XXXXXXXXXXX.\nII.	XXXXXXXXXXX.\nIII.	XXXXXXXXXXX', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'4 -    ANÁLISE ECONÔMICO-FINANCEIRO',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'         TEXTO 1 (empresa sem balanço ou só com balanço de abertura):\n\n\
		        Em razão da ausência de Balanço Patrimonial e Demonstrativo de Resultados do Exercício / Ou em caso de empresa com\
		menos de um ano de criação/funcionamento), consideram-se suficientes as projeções informadas no Plano de Negócios\
		à(s) fl(s). XX dos autos.\n\n\
		        TEXTO 2 (empresa sem balanço ou só com balanço de abertura):\n\n\
		        A empresa apresentou à fl. XX o seu Balanço de Abertura, cuja data de fechamento deu-se em XX/XX/XXXX. Como este\
		tipo de Balanço não permite a realização de cálculos de índices econômico-financeiros, calcularemos o Ponto de\
		Equilíbrio Contábil, fazendo uso das projeções situadas às fls. XX dos autos.\n\n\
		        a) Ponto de Equilíbrio Contábil = Custos Fixos / % Margem Contribuição:\n',align='J')
	pdf.set_font('Arial', 'B', 12)
	pdf.cell(57,10,'Item',1,0,'C')
	pdf.cell(38,10,'Atual (R$)',1,0,'C')
	pdf.cell(19,10,'%',1,0,'C')
	pdf.cell(57,10,'Projetada (R$)',1,0,'C')
	pdf.cell(19,10,'%',1,1,'C')
	pdf.set_font('Arial', '', 12)
	pdf.cell(57,5,'Receitas',1,0,'L')
	pdf.cell(38,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'100%',1,0,'C')
	pdf.cell(57,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'100%',1,1,'C')
	pdf.cell(57,5,'(-)Custos Variáveis',1,0,'L')
	pdf.cell(38,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'xx%',1,0,'C')
	pdf.cell(57,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'xx%',1,1,'C')
	pdf.cell(57,5,'= Margem de Contribuição',1,0,'L')
	pdf.cell(38,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'xx%',1,0,'C')
	pdf.cell(57,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'xx%',1,1,'C')
	pdf.cell(57,5,'(-) Custos Fixos',1,0,'L')
	pdf.cell(38,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'xx%',1,0,'C')
	pdf.cell(57,5,'xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'xx%',1,1,'C')
	pdf.cell(57,5,'P.E Contábil (R$)',1,0,'L')
	pdf.cell(38,5,'R$ xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'',1,0,'C')
	pdf.cell(57,5,'R$ xx.xxx,xx',1,0,'R')
	pdf.cell(19,5,'',1,1,'C')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'ANÁLISE:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        Considerando as previsões de vendas e custos, inclusive com suas respectivas elevações,\
		entende-se que seria necessário à requerente obter receitas aproximadas de R$ XXX.XXX,XX (por extenso) para não\
		incorrer em prejuízos, sendo tal valor o limite para cobrir os custos.\n\n Ou...\n\nTEXTO 3 (empresa com balanço)\n\n\
		        Para o cálculos dos índices seguintes, tomou-se como base o Balanço Patrimonial apresentado pela empresa,\
		encerrado em XX/XX/XXXX, situado à(s) fl(s) XX dos autos.',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'        A) Liquidez Corrente:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        Calculada a partir da Razão entre os direitos a curto prazo da empresa (Caixas, bancos,\
		estoques, clientes) e a as dívidas a curto prazo (Empréstimos, financiamentos, impostos, fornecedores). No Balanço\
		estas informações são evidenciadas respectivamente como Ativo Circulante e Passivo Circulante.\n\n        Liquidez Corrente=\
		Ativo Circulante / Passivo Circulante.',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'        B) Liquidez Seca:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        Similar a liquidez corrente a liquidez Seca exclui do cálculo acima os estoques, por não\
		apresentarem liquidez compatível com o grupo patrimonial onde estão inseridos. O resultado deste índice\
		será invariavelmente menor ao de liquidez corrente, sendo cauteloso com relação ao estoque para a liquidação\
		de obrigações.\n\n         Liquidez Seca= (Ativo circulante - Estoques) / Passivo circulante',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'        C) Liquidez Geral:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        Este índice leva em consideração a situação a longo prazo da empresa, incluindo no cálculo\
		os direitos e obrigações a longo prazo. Estes valores também são obtidos no balanço patrimonial.\n\n\
		        Observação: A partir de 31.12.2008, em função da nova estrutura dos balanços patrimoniais promovida pela\
		MP 449/2008, a fórmula da liquidez geral será:\n\n        Liquidez Geral = (Ativo circulante + Realizável a longo prazo)\
		/(Passivo Circulante + Passivo não circulante) ',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'ANÁLISE:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        Os indicadores resultantes dos cálculos realizados demonstram que a empresa analisada\
		teria, considerando a teoria aplicada, uma condição financeira saudável para quitar suas dívidas e cumprir\
		seus compromissos, a curto e longo prazo.',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'5 -    INVESTIMENTO FIXO APRESENTADO\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        De acordo com as informações do relatório em anexo (Anexo I), constante à(s) fl(s). XX, o\
		valor total da(s) nota(s) fiscal(is) considerada(s) válida(s) nesta análise inicial, e destinada(s) à\
		composição do ativo imobilizado da requerente é de R$ XXX.XXX,XX (por extenso), que servirá como sabe para o\
		incentivo de financiamento de ICMS conferido da Lei nº 1.358/00. (Deve-se fazer um resumo sobre as deduções\
		de itens das notas fiscais incompatíveis com a legislação, se houver).',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'5.1 -    TAXAS ADMINISTRATIVA:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'        Mantendo-se o valor do investimento fixo constante neste parecer, incidirá sobre ele a taxa\
		administrativa de 3% (três por cento) destinada à capitalização do Fundo de Desenvolvimento Sustentável - FDS,\
		com valor de R$ XXX.XXX,XX (por extenso), a ser recolhida através do Documento de Arrecadação Estadual - DAE.\n\
		        A empresa poderá ainda optar pelo parcelamento da taxa em até XX (XXX) vezes, com valor da parcela\
		fixado em R$ XXX,XX (por extenso), conforme critérios da Resolução COPIAI/AC n° 003 de 11 de julho de 2003,\
		publicada no D.O.E n° 8.577 de 14 de julho de 2003.', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'5.2 -    Nível de Redução de ICMS Apurado:\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.cell(90,5,'Critétrios de Avaliação',1,0,'C')
	pdf.cell(61.3,5,'Dados do Projeto',1,0,'C')
	pdf.cell(35.7,5,'Pontuação Obtida',1,1,'C')
	pdf.set_font('Arial', '',10)
	pdf.multi_cell(90,5,'Quanto a quantidade de empregos.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x+5)
	pdf.multi_cell(61.3,5,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x+5)
	pdf.multi_cell(35.7,5,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto ao porte da empresa.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x+5)
	pdf.multi_cell(61.3,5,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x+5)
	pdf.multi_cell(35.7,5,'',1,1,'C')
	pdf.multi_cell(90,5,'Percentual participativo da mão-de-obra direta e indireta agregada ao custo da produção.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x)
	pdf.multi_cell(61.3,x,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x)
	pdf.multi_cell(35.7,x,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à utilização de matéria-prima e material secundário local ou regional, dentro dos parâmetros\
		do desenvolvimento sustentável.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x-5)
	pdf.multi_cell(61.3,x+5,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x-5)
	pdf.multi_cell(35.7,x+5,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à produção de bens com ou sem similar no Estado.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x)
	pdf.multi_cell(61.3,x,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x)
	pdf.multi_cell(35.7,x,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à geração própria e alternativa de energia elétrica.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x)
	pdf.multi_cell(61.3,x,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x)
	pdf.multi_cell(35.7,x,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à utilização de equipamentos ou processos antipoluentes que\
		resguardem a proteção do meio-ambiente.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x-5)
	pdf.multi_cell(61.3,x+5,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x-5)
	pdf.multi_cell(35.7,x+5,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à localização do empreendimento em regiões administrativas \
		prioritárias e dentro dos parâmetros estabelecidos pelo ZEE.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x-5)
	pdf.multi_cell(61.3,x+5,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x-5)
	pdf.multi_cell(35.7,x+5,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à geração ou melhoria de novos produtos ou processos.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x)
	pdf.multi_cell(61.3,x,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x)
	pdf.multi_cell(35.7,x,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à formação de recursos humanos, objetivando a melhoria da qualidade e da produtividade.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x)
	pdf.multi_cell(61.3,x,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x)
	pdf.multi_cell(35.7,x,'',1,1,'C')
	pdf.multi_cell(90,5,'Quanto à existência de certificados qualificados como de manejo florestal sustentável, de origem,\
		de processo ou ambiental.',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+90,y-x-5)
	pdf.multi_cell(61.3,x+5,'',1,0,)
	pdf.set_xy(x+(90+61.3),y-x-5)
	pdf.multi_cell(35.7,x+5,'',1,1,'C')

	pdf.set_font('Arial','',12)
	pdf.multi_cell(190,5,'\n        Conforme o quadro acima, a empresa foi classificada na Faixa X, com XX pontos.\
		Dessa forma, o nível de redução a ser utilizado no abatimento dos saldos devedores do ICMS será de\
		XX% (por extenso), com prazo para ser utilizado até 31 de dezembro de 2035, conforme o art. 1º da Lei nº 2.956,\
		de 9 de abril de 2015, que alterou a Lei nº 1.358, de 29 de dezembro de 2000, e considerando o disposto\
		no Decreto nº 4.196 de 1º de outubro de 2001.', align='J')

	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'6 -    OBSERVAÇÕES COMPLEMENTARES\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)

	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'7 -    CONCLUSÃO\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'Finalizada a análise sobre o Plano de Negócios e a documentação apresentada,\
		somos por sua APROVAÇÃO (com ou sem ressalvas) e o seu prosseguimento para a deliberação nas demais\
		instituições que compõem a Câmara Técnica, além da própria COPIAI/AC, considerando a(s) observação(ões)\
		disposta(s) no item X deste parecer.', align='J')

	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'É o Parecer.\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'Rio Branco-AC xx de xxxxx de xxxx\n',align='R')
	pdf.ln(5)
	pdf.multi_cell(190,5,'Nome do Analista\nCargo/Função na COPIAI/AC',align='C')
	pdf.ln(5)
	pdf.multi_cell(190,5,'De Acordo\n Rio Branco, xx/xx/xxxx.',align='R')
	pdf.ln(5)
	pdf.multi_cell(190,5,'Nome do Chefe Imediato\nCargo/Função na COPIAI/AC',align='R')

	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado

@app.route('/api/roteiro', methods=['GET'])
def impressaoRoteiro():
	class PDF(FPDF):
		def footer(self):
			self.set_y(-20)
			self.set_font('Arial','I', 8)
			# self.multi_cell(0,10,'Página '+str(self.page_no())+'/{nb}',0,0,'L')

	pdf = PDF()
	pdf.add_page()
	# pdf.alias_nb_pages()
	pdf.ln(5)
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(190,5,'ROTEIRO BÁSICO PARA O PLANO DE NEGÓCIOS\n\
		(Este é um roteiro contendo as informações mínimas que deverão ser prestadas e, de acordo com cada\
		empreendimento, deverá ser detalhado).',align='C')
	pdf.multi_cell(190,5,'        \nTodos os quadros demonstrativos deverão ser acompanhados das respectivas memórias\
		de cálculo.',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'1 -    INTRODUÇÃO\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'(Definir tipo de beneficiamento a ser pleitado)', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'2  -    A EMPRESA\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'  2.1 - Razão Social\n\
		2.2 - Nome de Fantasia\n\
		2.3 - Ramo de Atividade\n\
		2.4 - Objetivo Social\n\
		2.5 - Forma Jurídica\n\
		2.6 - Sede e Foro\n\
		2.7 - Endereço\n\
		2.7.1 - Escritório\n\
		        Telefone\n\
		        E-mail\n\
		2.7.2 - Fábrica\n\
		        Telefone\n\
		        E-mail\n\
		2.8 - Registros\n\
		        C.N.P.J:\n\
		        Inscrição Estadual:\n\
		        Junta Comercial:\n\
		Data da Constituição:\n\
		2.9 - Nº de filiais (se for o caso)\n\
		        Quantidade:\n\
		        Endereço da Sede:\n\
		2.10 - A Missão da Empresa\n\
			(Qual é realmente seu negócio? Qual sua filosofia de trabalho?)\n\
		2.11 - Controle do Capital Atual da Empresa (No caso de Cooperativa preencher quadro 2.12).\n', align='J')
	pdf.ln(5)
	pdf.cell(63.3,10,'Nome',1,0,'C')
	pdf.cell(53.3,10,'Nacionalidade',1,0,'C')
	pdf.cell(73.3,5,'Ações/Quotas',1,1,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+116.6,y)
	pdf.cell(24.43,5,'Quant.',1,0,'C')
	pdf.cell(24.43,5,'V.Total.',1,0,'C')
	pdf.cell(24.43,5,'%',1,1,'C')
	pdf.set_font('Arial','',10)
	pdf.cell(63.3,5,'',1,0,'L')
	pdf.cell(53.3,5,'',1,0,'L')
	pdf.cell(24.43,5,'',1,0,'L')
	pdf.cell(24.43,5,'',1,0,'L')
	pdf.cell(24.43,5,'',1,1,'L')
	pdf.set_font('Arial','',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'2.12 - Dirigentes da Empresa/COOPERATIVA', align='J')
	pdf.ln(3)
	pdf.cell(71.25,5,'NOME E ENDEREÇO',1,0,'C')
	pdf.cell(23.75,5,'NAC.',1,0,'C')
	pdf.cell(47.5,5,'CARGO',1,0,'C')
	pdf.cell(47.5,5,'CPF Nº',1,1,'C')
	pdf.cell(71.25,5,'',1,0,'C')
	pdf.cell(23.75,5,'',1,0,'C')
	pdf.cell(47.5,5,'',1,0,'C')
	pdf.cell(47.5,5,'',1,1,'C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'2.13 - Capacidade Empresarial dos Dirigentes\n\
		(relatar experiencia do empresário)\n\n\
		2.14 - Regime de Tributação\n\
		(informar tipo de tributação, se SIMPLES, normal, etc.)\n\n\
		2.15 - Informar recolhimento de ICMS do último exercício.\n\n\
		2.16 - Incentivos e/ou Benefícios Fiscais já Existentes (nos âmbitos federal, estadual e municipal, se for o caso).\n\n\
		2.17 - Financiamento obtido\n\
		(informar se a empresa possui algum tipo financiamento e valor financiado: BNDES, FNO, ETC).\n\
		', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'3 -    PROJETO\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'3.1 - Objetivo do Projeto\n\
        (Se implantação, modernização, ampliação)\n\n\
		3.2 - Metas a alcançar\n\
        (Demonstrar forma de atingir o objetivo do projeto)\n\n\
	', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'4 -    LOCALIZAÇÃO\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'4.1 - Aspectos Mercadológicos\n\
        (Definir público-alvo; localização do empreendimento, etc.)\n\n\
		4.2 - Aspectos Legais\n\
        (Verificar se o local é adequado para instalação, ou seja, se está dentro do ZEE ou não)\n\n\
		4.3 - Aspectos Técnicos e Operacionais\n\
        (Relatar sobre a matéria-prima, sua localização, fornecedores, dificuldades de obtê-la)\n\n\
	', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'5 -    MERCADO\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'  5.1 - O Produto: razões que levaram a produzir estes produtos.\n\n\
		5.2 - Vantagens dos produtos em relação aos concorrentes\n\n\
		5.3 - Mercado Consumidor (discriminar principais clientes)\n\n\
		5.4 - Mercado Concorrente (discriminar principais concorrentes)\n\n\
		5.5 - Mercado Fornecedor (discriminar principais fornecedores de insumos)\n\n\
		5.6 - Abrangência do Mercado\n\n\
	', align='J')
	pdf.cell(47.5,10,'PRODUTOS',1,0,'C')
	pdf.cell(142.5,5,'MERCADO (%)',1,1,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+47.5,y)
	pdf.cell(35.625,5,'Local',1,0,'C')
	pdf.cell(35.625,5,'Regional',1,0,'C')
	pdf.cell(35.625,5,'Nacional',1,0,'C')
	pdf.cell(35.625,5,'Externo',1,1,'C')
	pdf.cell(47.5,5,'Produto 1',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.multi_cell(190,5,'Obs: Regional, Nacional e Externo, discriminar no rodapé do quadro as localidades.\n\
		5.7 - Período de Comercialização\n\n',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'6 -    MARKETING\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'Explicar como pretende fazer ou faz para convencer os clientes a comprar da empresa. \
		pode-se incluir nesse ponto:\n\
		a) Como tornará ou tornou seus clientes conhecedores da existência de seus produtos ou serviços?\n\n\
		b) Que mensagem ou pretende utilizar para criar desejo de compra?\n\n\
		c) Que métodos utiliza ou utilizará para transmitir esta mensagem?\n\n\
		d) Como irá estruturar suas vendas ou como a estrutura?\n\n\
	',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'7 -    ASPECTOS TÉCNICOS DA EMPRESA\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'7.1 - Descrição dos Produtos Fabricados.\n\n\
		7.3 - Descrição da Área Demandada (dimensões, tipo de edificações, etc.)\n\n\
		7.4 - Descrição da Infra Estrutura de Acesso, Energia e Comunicação.\n\n\
		7.5 - Utilização da Capacidade Instalada e/ou a Instalar atual e projetada para até dois anos.\n\n\
		Atual:     ______ %\n\
		Projetada\n\
		1º Ano:   ______ %\n\
		2º Ano    ______ %\n\
		3º Ano    ______ %\n\n\
		7.6 - Regime de Trabalho\n\
		______ horas/dia\n\
		______ dias por mês\n\
		______ meses por ano\n\n\
		7.7 - Imobilizações Existentes. Descrever o imobilizado da empresa a partir de 1º de outubro de 2000\
		(excluído terreno e veículo de passeio).\n\n\
		7.8 - Manufatura e Produção\n\
		Explicar o processo e equipamentos utilizados ou que pretende utilizar para fabricar ou prestar serviços.\
		Ou seja, fazer um passo a passo do processo utilizado para fabricar ou prestar serviços (o que é feito, quem faz,\
		o equipamento / imobilizações, o material envolvido, fonte de energia utilizada e sua previsão de demanda,\
		tratamento dos resíduos e certificações).\n\n\
		7.8.1 - Previsão de Procedência da Matéria Prima e Material Secundário a serem Utilizados dentro \
		dos Parâmetros de Desenvolvimento Sustentável\n\
	',align='J')
	pdf.set_font('Arial','',10)
	pdf.cell(31.6,10,'Insumos',1,0,'C')
	pdf.cell(15.83,10,'Origen',1,0,'C')
	pdf.cell(15.83,10,'Unid.',1,0,'C')
	pdf.cell(31.6,10,'Custo Unitário',1,0,'C')
	pdf.cell(47.43,5,'Atual',1,0,'C')
	pdf.cell(47.43,5,'Projetada',1,1,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+94.86,y)
	pdf.cell(23.785,5,'Quant.',1,0,'C')
	pdf.cell(23.785,5,'Valor',1,0,'C')
	pdf.cell(23.785,5,'Quant.',1,0,'C')
	pdf.cell(23.785,5,'Valor',1,1,'C')
	pdf.cell(31.6,5,'',1,0,'C')
	pdf.cell(15.83,5,'',1,0,'C')
	pdf.cell(15.83,5,'',1,0,'C')
	pdf.cell(31.6,5,'',1,0,'C')
	pdf.cell(23.785,5,'',1,0,'C')
	pdf.cell(23.785,5,'',1,0,'C')
	pdf.cell(23.785,5,'',1,0,'C')
	pdf.cell(23.785,5,'',1,1,'C')
	pdf.ln(5)
	pdf.set_font('Arial','',12)
	pdf.multi_cell(190,5,'7.8.2 - Necessidade de mão de obra anual',align='J')
	pdf.ln(5)
	pdf.set_font('Arial','',10)
	pdf.cell(47.43,10,'Discriminação/Atividade',1,0,'C')
	pdf.cell(47.43,10,'Salário Unitário Mensal',1,0,'C')
	pdf.cell(47.43,5,'Quantidade',1,0,'C')
	pdf.cell(47.43,5,'Custo Mensal',1,1,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+94.86,y)
	pdf.cell(23.785,5,'Quant.',1,0,'C')
	pdf.cell(23.785,5,'Valor',1,0,'C')
	pdf.cell(23.785,5,'Quant.',1,0,'C')
	pdf.cell(23.785,5,'Valor',1,1,'C')
	pdf.cell(47.43,5,'1-Sócios / Prolabore',1,0,'L')
	pdf.cell(47.43,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.cell(94.86,5,'Sub. Total',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.cell(47.43,5,'2- Mão-de-obra Fixa',1,0,'L')
	pdf.cell(47.43,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.cell(94.86,5,'Sub. Total',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.cell(47.43,5,'3- Mão-de-obra Variavel',1,0,'L')
	pdf.cell(47.43,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.cell(94.86,5,'Sub. Total',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.cell(94.86,5,'Total Geral',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,0,'L')
	pdf.cell(23.785,5,'',1,1,'L')
	pdf.ln(5)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'7.8.3 - Previsão de Procedência da Energia a ser Consumida no Empreendimento (concessionária\
		local ou alternativa/própria)\n\n\
		7.8.4 - Previsão de Utilização de Equipamentos ou Processos Antipoluentes que Resguardem a Proteção do\
		Meio Ambiente (tratamento, eliminação ou reaproveitamento de resíduos)\n\n\
		7.8.5 - Quanto à formação de recursos humanos, objetivando a melhoria da qualidade e da produtividade\
		(política de treinamento anual de funcionários no sentido de aperfeiçoar ou flexibilizar a capacidade de trabalho).\n\n\
		7.8.6 - Certificados ou Processo/Projeto de Origem de Produção Sustentável\
	',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'8 -    FATURAMENTO E CUSTOS\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'Preencher o quadro a seguir.',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'8.1 - Modelo do Quadro Estrutura de Custos Totais Anuais\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(47.5,10,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(47.5,10,'ATUAL',1,0,'C')
	pdf.cell(95,5,'PROJETADO',1,1,'C')
	x1=pdf.get_x()
	y1=pdf.get_y()
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y)
	pdf.cell(47.5,5,'1º ANO',1,0,'C')
	pdf.cell(47.5,5,'2º ANO',1,1,'C')
	pdf.multi_cell(47.5,4,'1 - Custos Variáveis\n\
		- Mão de obra direta\n\
		- Encargos\n\
		- Matéria Prima\n\
		- Materiais Secundários\n\
		- Utilidades\n\
		- (Energia Elétrica, vapor, água industrial e potável, combustível)\n\
		- Mat. auxiliares (se for o caso)\n\
		- Outros diversos (variar de 2 a 5%, dependendo do tamanho da empresa)\
	',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+47.5,y1+5)
	pdf.cell(47.5,56,'',1,0,'C')
	pdf.cell(47.5,56,'',1,0,'C')
	pdf.cell(47.5,56,'',1,1,'C')
	pdf.multi_cell(47.5,5,'TOTAL DOS CUSTOS VARIÁVEIS',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+47.5,y-10)
	pdf.cell(47.5,10,'',1,0,'C')
	pdf.cell(47.5,10,'',1,0,'C')
	pdf.cell(47.5,10,'',1,1,'C')
	pdf.multi_cell(47.5,4,'2 - Custos Fixos\n\
		- Mão de obra\n\
		- Encargos de mão de obra\n\
		- Manutenção / conservação\n\
		- Depreciação (prédio, computadores, instalações, máquinas equipamentos do ativo operacional da indústria.)\n\
		- Outros/Diversos ( 2 a 5%)\
	',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+47.5,y-48)
	pdf.cell(47.5,48,'',1,0,'C')
	pdf.cell(47.5,48,'',1,0,'C')
	pdf.cell(47.5,48,'',1,1,'C')
	pdf.multi_cell(47.5,5,'TOTAL DOS CUSTOS FIXOS',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+47.5,y-10)
	pdf.cell(47.5,10,'',1,0,'C')
	pdf.cell(47.5,10,'',1,0,'C')
	pdf.cell(47.5,10,'',1,1,'C')
	pdf.multi_cell(47.5,10,'TOTAL GERAL',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+47.5,y-10)
	pdf.cell(47.5,10,'',1,0,'C')
	pdf.cell(47.5,10,'',1,0,'C')
	pdf.cell(47.5,10,'',1,1,'C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'Obs.: Honorários da diretoria - Deverá ser incluído em Despesas Administrativas no\
		quadro 8.3 - Demonstrativo de Resultados da Empresa', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'8.2 - Programa Anual de Produção e Vendas.\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(30.5,20,'PRODUTOS',1,0,'C')
	pdf.cell(23.75,20,'UNID.',1,0,'C')
	pdf.cell(50.375,15,'ATUAL ANO X',1,0,'C')
	pdf.cell(85.375,5,'PROJETADA',1,1,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+104.625,y)
	pdf.cell(33.4583,10,'Quantidade',1,0,'C')
	pdf.cell(18.4583,15,'Preço Unit.',1,0,'C')
	pdf.cell(33.4583,10,'Receita',1,1,'C')
	pdf.set_xy(x+104.625,y+10)
	pdf.cell(16.72915,5,'Ano 1',1,0,'C')
	pdf.cell(16.72915,5,'Ano 2',1,1,'C')
	# pdf.cell(28.4583,5,'Receita',1,1,'C')
	pdf.set_xy(x+156.5416,y+10)
	pdf.cell(16.72915,5,'Ano 1',1,0,'C')
	pdf.cell(16.72915,5,'Ano 2',1,1,'C')
	pdf.set_xy(x+54.25,y+10)
	pdf.cell(25.1875,5,'Quantidade',1,0,'C')
	pdf.cell(25.1875,5,'Receita',1,1,'C')
	pdf.cell(30.5,20,'',1,0,'L')
	pdf.cell(23.75,20,'',1,0,'L')
	pdf.cell(25.1875,20,'',1,0,'L')
	pdf.cell(25.1875,20,'',1,0,'L')
	pdf.cell(16.72915,20,'',1,0,'L')
	pdf.cell(16.72915,20,'',1,0,'L')
	pdf.cell(18.4583,20,'',1,0,'L')
	pdf.cell(16.72915,20,'',1,0,'L')
	pdf.cell(16.72915,20,'',1,1,'L')
	pdf.set_auto_page_break(auto=True)
	pdf.add_page('L')
	pdf.ln(3)
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'8.3 - Demonstrativo de Resultados da Empresa\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(95,10,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(50,10,'PERÍODO BASE',1,0,'C')
	pdf.cell(130,5,'PROJETADO',1,1,'C')
	x1=pdf.get_x()
	y1=pdf.get_y()
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+145,y)
	pdf.cell(65,5,'1º ANO',1,0,'C')
	pdf.cell(65,5,'2º ANO',1,1,'C')
	pdf.cell(95,5,'1 - Receita Operacional Bruta',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'2 - ( - ) Impostos e deduções (Quebras e avarias)',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'3 - ( = ) Receita operacional Líquida',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'4 - ( - ) Custos dos Produtos Vendidos (Custos Industriais)',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'5 - ( = ) Lucro Bruto',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'6 - ( - ) Despesas Operacionais',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'6.1 - Comerciais',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'6.2 - Administrativa',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.multi_cell(95,10,'6.3 - Financeiras\n\
		*   S/ Operação\n\
		*   S/ Financiamento\n\
	',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-40)
	pdf.cell(50,30,'',1,0,'L')
	pdf.cell(65,30,'',1,0,'L')
	pdf.cell(65,30,'',1,1,'L')
	pdf.cell(95,5,'7 - ( - ) Amortização do Ativo Deferido',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'8 - ( = ) Resultado Operacional',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'9 - (mais/menos) Resultado Não Operacional',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'10 - ( = ) Lucro Autos do IR',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'11 - ( - )  Previsão p/ o IR',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'12 - ( = ) Resultado ou Lucro do Exercício',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.cell(95,5,'',1,0,'L')
	pdf.cell(50,5,'',1,0,'L')
	pdf.cell(65,5,'',1,0,'L')
	pdf.cell(65,5,'',1,1,'L')
	pdf.ln(3)
	pdf.set_auto_page_break(auto=True)
	pdf.add_page()
	pdf.set_font('Arial', 'B', 12)
	pdf.multi_cell(190,5,'9 - O Financiamento\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'9.1 - Linha de Financiamento (Programa)\n\n\
		9.2 - Valor do Financiamento\n\n\
		9.3 - Prazo Solicitado\n\n\
		9.4 - Justificativa da Solicitação\n\n\
		9.5 - Plano de Aplicação\n\
	',align='J')
	pdf.multi_cell(190,5,'9.1 - Linha de Financiamento (Programa)\n\n\
		9.2 - Valor do Financiamento\n\n\
		9.3 - Prazo Solicitado\n\n\
		9.4 - Justificativa da Solicitação\n\n\
		9.5 - Plano de Aplicação\n\n\
	',align='J')
	pdf.set_font('Arial', '',10)
	pdf.cell(95,5,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(95,5,'VALOR',1,1,'C')
	pdf.multi_cell(95,5,'  ATIVO FIXO\n\n\
		1 - Construção Civil\n\
		2 - Instalações Complementares\n\
		3 - Máquinas e Equipamentos\n\
		4 - Equipamentos de Informática\n\
		5 - Veículos\n\
		6 - \n\
		7 - \n\n\
		CAPITAL DE GIRO\n\
		DESPESAS PRÉ-OPERACIONAIS\n\n\
		1 - Elaboração do Projeto\n\
		2 - Fretes e Carretos\n\
		3 - \n\
		4 - \n\
		Eventuais\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-90)
	pdf.cell(95,90,'',1,1,'C')
	pdf.cell(95,5,'TOTAL',1,0,'C')
	pdf.cell(95,5,'',1,1,'C')
	pdf.ln(3)
	pdf.multi_cell(190,5,'Obs.: Relacionar todos os itens com descrição suscinta.', align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'10 - GARANTIAS\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',12)
	pdf.multi_cell(190,5,'a) Detalhar os bens a serem oferecidos em garantia  informando os respectivos valores.\n\
		b) Em caso de terrenos anexar cópia da escritura e registro no Cartório de Imóveis.\n\
		c) Se edificações, anexar registros de averbações (Prefeitura), registro no Cartório de Imóveis e CND do INSS.\n\
		d) Se máquinas e equipamentos especificar marca, modelo, nº de série, fornecedor e cópia da nota fiscal.\n\
		e) Outros - Especificar.\n\
	',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'11 - Indicadores do Capital de Giro\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(95,5,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(95,5,'INDICADORES - PROJETADO',1,1,'C')
	pdf.cell(95,5,'1 - USOS',1,0,'L')
	pdf.cell(95,5,'',1,1,'L')
	pdf.cell(95,5,'1.2 - Caixa Mínima (Número de Dias)',1,0,'L')
	pdf.cell(95,5,'',1,1,'L')
	pdf.multi_cell(95,5,'1.2 - Financiamento de Vendas\n\
		- Prazo Médio de Financiamento em dias\n\
		- % de Vendas a prazo\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-15)
	pdf.cell(95,15,'',1,1,'C')
	pdf.multi_cell(95,5,'1.3 - Estoques\n\
		1.3.1  - Matéria-prima\n\
		   - Nº de dias de estoque mínimo\n\
		1.3.2  - Materiais Secundários\n\
		   - Nº de dias de estoque mínimo\n\
		1.3.3	- Material de Embalagem\n\
		   - Nº de dias de estoque mínimo\n\
		1.3.4	- Combustíveis e Lubrificantes\n\
		   - Nº de dias de estoque mínimo\n\
		1.3.5	- Produtos em Processos\n\
		   - Nº de dias de estoque mínimo\n\
		   - Nº de dias efetivo de funcionamento/ano\n\
		1.3.6	- Produtos Acabados\n\
		   - Nº de dias de estoque mínimo\n\
		1.3.7	- Peças e Materiais de Reposição\n\
		- % sobre total de máquinas e equipamentos\n\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-85)
	pdf.cell(95,85,'',1,1,'C')
	pdf.cell(95,5,'2 - Fontes',1,0,'L')
	pdf.cell(95,5,'',1,1,'L')
	pdf.multi_cell(95,5,'    2.1 - Crédito de Fornecedores\n\
		- % de compras a prazo\n\
		- Prazo médio de Pagamento\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-15)
	pdf.cell(95,15,'',1,1,'C')
	pdf.multi_cell(95,5,'    2.2 - Desconto de Recebíveis\n\
		- % de compras a prazo\n\
		- % de descontos\n\
		- Prazo médio concedido em dias\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-20)
	pdf.cell(95,20,'',1,1,'C')
	pdf.multi_cell(95,5,'    2.3 - Salários\n\
		- Prazo médio de Pagamento em dias\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-10)
	pdf.cell(95,10,'',1,1,'C')
	pdf.multi_cell(95,5,'    2.4 - Impostos e Encargos Sociais\n\
		- Prazo médio de Recolhimento em dias\
	',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+95,y-10)
	pdf.cell(95,10,'',1,1,'C')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'12 - Demonstrativo de Necessidades Financeiras\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(85,5,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(30,5,'PROJETADO',1,0,'C')
	pdf.cell(40,5,'EXISTENTE BALANÇO',1,0,'C')
	pdf.cell(30,5,'A RELIZAR',1,1,'C')
	pdf.multi_cell(85,5,'1 - USOS\n1.1 - Caixa Mínima',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-10)
	pdf.cell(30,10,'',1,0,'C')
	pdf.cell(40,10,'',1,0,'C')
	pdf.cell(30,10,'',1,1,'C')
	pdf.cell(85,5,'1.2 - Financiamento de Vendas',1,0,'L')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(30,5,'',1,1,'C')
	pdf.multi_cell(85,5,'1.3 - ESTOQUES\n\
		-   Matéria-prima\n\
		-   Materiais secundários\n\
		-   Material de embalagem\n\
		-   Combustíveis e lubrificantes\n\
		-   Produtos em processos\n\
		-   Produtos acabados\n\
		-   Peças e materiais de reposição\
	',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-40)
	pdf.cell(30,40,'',1,0,'C')
	pdf.cell(40,40,'',1,0,'C')
	pdf.cell(30,40,'',1,1,'C')
	pdf.multi_cell(85,5,'2 - FONTES\n2.1 - Crédito de Fornecedores',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-10)
	pdf.cell(30,10,'',1,0,'C')
	pdf.cell(40,10,'',1,0,'C')
	pdf.cell(30,10,'',1,1,'C')
	pdf.cell(85,5,'2.2 - Descontos Recebíveis',1,0,'L')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(30,5,'',1,1,'C')
	pdf.cell(85,5,'2.3 - Salários',1,0,'L')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(30,5,'',1,1,'C')
	pdf.cell(85,5,'2.5 - Impostos e Encargos Sociais',1,0,'L')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(30,5,'',1,1,'C')
	pdf.cell(85,5,'3 - CAPITAL DE GIRO',1,0,'L')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(30,5,'',1,1,'C')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'13 - Usos e Fontes do Projeto\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(85,10,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(30,10,'PROJETADO',1,0,'C')
	pdf.multi_cell(40,5,'REALIZADO ATÉ \n___/___/_____',1,0,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+155,y-10)
	pdf.cell(30,10,'A RELIZAR',1,1,'C')
	pdf.multi_cell(85,5,'1 - USOS\n\
		1.1 - ATIVO FIXO\n\
		- Terreno\n\
		- Construção Civil\n\
		- Instalações Complementares\n\
		- Máquinas e Equipamentos\n\
		- Equipamentos de Informática\n\
		- Móveis e Utensílios\n\
		- Veículos\n\
		- 	\
	',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-50)
	pdf.cell(30,50,'',1,0,'C')
	pdf.cell(40,50,'',1,0,'C')
	pdf.cell(30,50,'',1,1,'C')
	pdf.multi_cell(85,5,'1.2 - CAPITAL DE GIRO\n\
		- Caixa Mínima\n\
		- Financiamento de Vendas\n\
		- Matéria-prima\n\
		- Materiais Secundários\n\
		- Material de Embalagem\n\
		- Combustíveis e Lubrificantes\n\
		- Produtos em Elaboração\n\
		- Produtos Acabados\n\
		- Peças e Material de Reposição',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-50)
	pdf.cell(30,50,'',1,0,'C')
	pdf.cell(40,50,'',1,0,'C')
	pdf.cell(30,50,'',1,1,'C')
	pdf.multi_cell(85,5,'1.3 - DESPESAS PRÉ-OPERACIONAIS\n\
		- Elaboração do Projeto\n\
		- Fretes e Carretos',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-15)
	pdf.cell(30,15,'',1,0,'C')
	pdf.cell(40,15,'',1,0,'C')
	pdf.cell(30,15,'',1,1,'C')
	pdf.multi_cell(85,5,'2 - FONTES\n\
		   2.1 - Programa de Incentivo (especificar)\n\
		   - Ativo Fixo\n\
		   - Capital de Giro\n\
		   - Despesas Pré-operacionais',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-25)
	pdf.cell(30,25,'',1,0,'C')
	pdf.cell(40,25,'',1,0,'C')
	pdf.cell(30,25,'',1,1,'C')
	pdf.multi_cell(85,5,'2.2 - Instituição Bancária (especificar)\n\
		- Ativo Fixo\n\
		- Capital de Giro\n\
		- Despesas Pré-operacionais',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-20)
	pdf.cell(30,20,'',1,0,'C')
	pdf.cell(40,20,'',1,0,'C')
	pdf.cell(30,20,'',1,1,'C')
	pdf.multi_cell(85,5,'2.3 - Outras Fontes (especificar)\n\
		- Ativo Fixo\n\
		- Capital de Giro',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-15)
	pdf.cell(30,15,'',1,0,'C')
	pdf.cell(40,15,'',1,0,'C')
	pdf.cell(30,15,'',1,1,'C')
	pdf.multi_cell(85,5,'2.4 - Empresa\n\
		- Ativo Fixo\n\
		- Capital de Giro\n\
		- Despesas Pré-operacionais\n\
		- ',1,0,'L')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+85,y-25)
	pdf.cell(30,25,'',1,0,'C')
	pdf.cell(40,25,'',1,0,'C')
	pdf.cell(30,25,'',1,1,'C')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.set_auto_page_break(auto=True)
	pdf.add_page('L')
	pdf.multi_cell(190,5,'14 - Fluxo de Caixa\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(100,10,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(165,5,'PROJETADO',1,1,'C')
	x1=pdf.get_x()
	y1=pdf.get_y()
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+100,y)
	pdf.cell(55,5,'ATUAL',1,0,'C')
	pdf.cell(55,5,'1º ANO',1,0,'C')
	pdf.cell(55,5,'2º ANO',1,1,'C')
	pdf.cell(100,5,'ENTRADAS',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Receita Operacional',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Financiamento Pretendido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Recursos Próprios Investido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Depreciação mais Amortização',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Outros Recursos de Terceiros Investidos',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'SAÍDAS',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Investimentos',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Despesas Operacionais',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Imposto de Renda e Contribuição Social',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Juros Sobre Financiamento Pretendido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Juros Sobre Financiamento Existentes',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Juros Sobre Financiamento para Capital de Giro',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Amortização do Financiamento Pretendido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Amortização de Financiamentos Existentes',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Amortização de Financiamentos para Capital de Giro',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'FLUXO DE CAIXA ECONÔMICO',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'FLUXO DE CAIXA OPERACIONAL',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.set_auto_page_break(auto=True)
	pdf.add_page('L')
	pdf.cell(100,10,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(165,5,'PROJETADO',1,1,'C')
	x1=pdf.get_x()
	y1=pdf.get_y()
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+100,y)
	pdf.cell(55,5,'ATUAL',1,0,'C')
	pdf.cell(55,5,'1º ANO',1,0,'C')
	pdf.cell(55,5,'2º ANO',1,1,'C')
	pdf.cell(100,5,'ENTRADAS',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Receita Operacional',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Financiamento Pretendido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Recursos Próprios Investido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Depreciação mais Amortização',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Outros Recursos de Terceiros Investidos',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'SAÍDAS',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Investimentos',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Despesas Operacionais',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Imposto de Renda e Contribuição Social',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Juros Sobre Financiamento Pretendido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Juros Sobre Financiamento Existentes',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Juros Sobre Financiamento para Capital de Giro',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Amortização do Financiamento Pretendido',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Amortização de Financiamentos Existentes',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'   Amortização de Financiamentos para Capital de Giro',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'FLUXO DE CAIXA ECONÔMICO',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.cell(100,5,'FLUXO DE CAIXA OPERACIONAL',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,0,'L')
	pdf.cell(55,5,'',1,1,'L')
	pdf.set_auto_page_break(auto=True)
	pdf.add_page()
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'15 - Avaliação do Projeto\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.multi_cell(190,5,'15.1 - Ponto de Nivelamento',align='J')
	pdf.cell(71.25,10,'DISCRIMINAÇÃO',1,0,'C')
	pdf.cell(47.5,10,'PERÍODO BASE',1,0,'C')
	pdf.cell(71.25,5,'PROJEÇÕES',1,1,'C')
	x=pdf.get_x()
	y=pdf.get_y()
	pdf.set_xy(x+118.75,y)
	pdf.cell(35.625,5,'Ano 1',1,0,'C')
	pdf.cell(35.625,5,'Ano 2',1,1,'C')
	pdf.cell(71.25,5,'- Custo Fixo Industrial',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'- Despesa Comercial Fixa',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'- Despesa Administrativa',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'- Despesa Financeira',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'1 - Total de Custo Fixo',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,' - Custo Industrial Variável',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'2 - Total Custo Variável',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'3 - Unidades Produzidas',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'4 - Custo Variavel Unitário',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'5 - Preço Unitário de Venda',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'6 - Margem de Contribuição (5) - (4)',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'7 - Ponto de Equilíbrio (1):(6)',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'8 - Capacidade de Produção',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.cell(71.25,5,'9 - % de Equilíbrio (7):(8)',1,0,'L')
	pdf.cell(47.5,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,0,'L')
	pdf.cell(35.625,5,'',1,1,'L')
	pdf.ln(3)
	pdf.multi_cell(190,5,'  15.2 - Taxa Interna de Retorno\n\
		15.3 - Lucratividade\n\
		15.4 - Rentabilidade\n\
		15.5 - Tempo de Retorno do Investimento\n\
		15.6 - Méritos do Projeto\n\
	',align='J')
	pdf.set_font('Arial', 'B',12)
	pdf.ln(3)
	pdf.multi_cell(190,5,'16 - Planilha de Simulação de Amortização\n',align='J')
	pdf.ln(3)
	pdf.set_font('Arial', '',10)
	pdf.cell(63.33, 5, 'Valor do Financiamento', 1,0,'L')
	pdf.cell(63.33, 5, '', 1,0,'L')
	pdf.cell(63.33, 5, '', 1,1,'L')
	pdf.cell(63.33, 5, 'TJLP', 1,0,'L')
	pdf.cell(63.33, 5, '0,000%', 1,0,'L')
	pdf.cell(63.33, 5, 'a.a', 1,1,'L')
	pdf.cell(63.33, 5, 'Juros(ao ano)', 1,0,'L')
	pdf.cell(63.33, 5, '0,000%', 1,0,'L')
	pdf.cell(63.33, 5, 'a.a', 1,1,'L')
	pdf.cell(63.33, 5, 'Prazo de Carência', 1,0,'L')
	pdf.cell(63.33, 5, '', 1,0,'L')
	pdf.cell(63.33, 5, 'meses', 1,1,'L')
	pdf.cell(63.33, 5, 'Prazo de Amortização', 1,0,'L')
	pdf.cell(63.33, 5, '', 1,0,'L')
	pdf.cell(63.33, 5, 'meses', 1,1,'L')
	pdf.cell(63.33, 5, 'Prazo Total', 1,0,'L')
	pdf.cell(63.33, 5, '', 1,0,'L')
	pdf.cell(63.33, 5, 'meses', 0,1,'L')
	pdf.ln(5)
	pdf.cell(38,5,'ANO', 1,0,'C')
	pdf.cell(38,5,'Saldo Devedor', 1,0,'C')
	pdf.cell(38,5,'Amortização', 1,0,'C')
	pdf.cell(38,5,'Juros', 1,0,'C')
	pdf.cell(38,5,'Parcela', 1,1,'C')
	for i in range(10):
		for i in range(12):
			pdf.set_font('Arial', '',10)
			pdf.cell(38,5,str(i+1), 1,0,'C')
			pdf.cell(38,5,'', 1,0,'C')
			pdf.cell(38,5,'', 1,0,'C')
			pdf.cell(38,5,'', 1,0,'C')
			pdf.cell(38,5,'', 1,1,'C')
		pdf.set_font('Arial', '',10)
		pdf.cell(76,5,'TOTAL ANUAL', 1,0,'C')
		pdf.cell(38,5,'', 1,0,'C')
		pdf.cell(38,5,'', 1,0,'C')
		pdf.cell(38,5,'', 1,1,'C')
	pdf.set_auto_page_break(auto=True)
	pdf.add_page()
	pdf.set_font('Arial', 'B',72)
	pdf.multi_cell(190,50,'Anexo IV \n\nRoteiro Básico\n Para Plano de \nNegócio',1,align='C')
	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado

@app.route('/api/protocolo', methods=['GET'])
def gerar_protocolo():
	class PDF(FPDF):
		def header(self):
			self.set_font('Arial','', 8)
	pdf = PDF()
	pdf.add_page('L')
	pdf.set_font('Arial','B',10)
	pdf.multi_cell(270,5,'1. CADASTRO GERAL DE PROCESSOS/EMPRESAS',align='J')
	pdf.set_font('Arial','',8)
	pdf.cell(230,5,'PROCESSOS', 1,0,'C')
	pdf.cell(40,5,'EMPRESAS', 1,1,'C')
	pdf.cell(15,5,'Nº',1,0,'C')
	pdf.cell(20,5,'ANO',1,0,'C')
	pdf.cell(30,5,'Data Início',1,0,'C')
	pdf.cell(45,5,'Consultor/Responsável',1,0,'C')
	pdf.cell(30,5,'Espécie',1,0,'C')
	pdf.cell(30,5,'Benefício',1,0,'C')
	pdf.cell(30,5,'Status',1,0,'C')
	pdf.cell(30,5,'Localização',1,0,'C')
	pdf.cell(40,5,'Razão Social',1,1,'C')
	pdf.cell(15,5,'',1,0,'C')
	pdf.cell(20,5,'',1,0,'C')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(45,5,'',1,0,'C')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(30,5,'',1,0,'C')
	pdf.cell(40,5,'',1,1,'C')
	pdf.set_auto_page_break(auto=True)
	pdf.add_page('L')
	pdf.cell(40,5,'EMPRESAS',1,0,'C')
	pdf.cell(57.5,5,'REGISTROS',1,0,'C')
	pdf.cell(57.5,5,'NATUREZA JURÍDICA',1,0,'C')
	pdf.cell(57.5,5,'ATIVIDADE PRINCIPAL',1,0,'C')
	pdf.cell(57.5,5,'ABERTURA',1,1,'C')
	pdf.cell(40,5,'Nome Fantasia',1,0,'C')
	pdf.cell(28.75,5,'CNPJ',1,0,'C')
	pdf.cell(28.75,5,'Insc. Estadual',1,0,'C')
	pdf.cell(15.75,5,'Cód.',1,0,'C')
	pdf.cell(41.75,5,'Descrição',1,0,'C')
	pdf.cell(15.75,5,'Cód.',1,0,'C')
	pdf.cell(41.75,5,'Descrição',1,0,'C')
	pdf.cell(28.75,5,'Tipo',1,0,'C')
	pdf.cell(28.75,5,'Data',1,1,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(28.75,5,'',1,0,'C')
	pdf.cell(28.75,5,'',1,0,'C')
	pdf.cell(15.75,5,'',1,0,'C')
	pdf.cell(41.75,5,'',1,0,'C')
	pdf.cell(15.75,5,'',1,0,'C')
	pdf.cell(41.75,5,'',1,0,'C')
	pdf.cell(28.75,5,'',1,0,'C')
	pdf.cell(28.75,5,'',1,1,'C')
	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado

@app.route('/api/contatos', methods=['GET'])
def gerar_contatos():
	class PDF(FPDF):
		def header(self):
			self.set_font('Arial','', 8)
	pdf = PDF()
	pdf.add_page('L')
	pdf.set_font('Arial','B',10)
	pdf.multi_cell(270,5,'2. CONTATOS NAS EMPRESAS',align='J')
	pdf.set_font('Arial','',8)
	pdf.cell(80,5,'EMPRESAS', 1,0,'C')
	pdf.cell(80,5,'ATIVIDADE PRINCIPAL', 1,0,'C')
	pdf.cell(110,5,'CONTATOS', 1,1,'C')
	pdf.cell(40,5,'Razão Social',1,0,'C')
	pdf.cell(40,5,'Nome Fantasia',1,0,'C')
	pdf.cell(20,5,'Cód.',1,0,'C')
	pdf.cell(60,5,'Descrição',1,0,'C')
	pdf.cell(46.66,5,'Endereço/E-mail',1,0,'C')
	pdf.cell(26.66,5,'Fone/Fax',1,0,'C')
	pdf.cell(36.66,5,'Responsável',1,1,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(40,5,'',1,0,'C')
	pdf.cell(20,5,'',1,0,'C')
	pdf.cell(60,5,'',1,0,'C')
	pdf.cell(46.66,5,'',1,0,'C')
	pdf.cell(26.66,5,'',1,0,'C')
	pdf.cell(36.66,5,'',1,1,'C')
	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado

@app.route('/api/lei1361', methods=['GET'])
def gerar_lei1361():
	class PDF(FPDF):
		def header(self):
			self.set_font('Arial','', 8)
	pdf = PDF()
	pdf.add_page('L')
	pdf.set_font('Arial','B',10)
	pdf.multi_cell(270,5,'3. MONITORAMENTO PROJETOS DO FUNDO DE DESENVOLVIMENTO SUSTENTÁVEL \
		- FDS - LEI 1.361/00',align='J')
	pdf.set_font('Arial','',8)
	pdf.cell(270,5,'PROCESSOS', 1,1,'C')
	pdf.cell(10,5,'Nº', 1,0,'C')
	pdf.cell(15,5,'Ano', 1,0,'C')
	pdf.cell(20,5,'Tipo', 1,0,'C')
	pdf.cell(70,5,'Requerente', 1,0,'C')
	pdf.cell(155,5,'Objeto', 1,1,'C')
	pdf.cell(10,5,'', 1,0,'C')
	pdf.cell(15,5,'', 1,0,'C')
	pdf.cell(20,5,'', 1,0,'C')
	pdf.cell(70,5,'', 1,0,'C')
	pdf.cell(155,5,'', 1,1,'C')
	pdf.set_auto_page_break(auto=True)
	pdf.add_page('L')
	pdf.cell(90,5,'RESOLUÇÕES',1,0,'C')
	pdf.cell(90,5,'DIÁRIO OFICIAL',1,0,'C')
	pdf.cell(90,5,'RECURSOS',1,1,'C')
	pdf.cell(10,5,'Nº', 1,0,'C')
	pdf.cell(25,5,'Data', 1,0,'C')
	pdf.cell(55,5,'Espécie', 1,0,'C')
	pdf.cell(45,5,'Nº', 1,0,'C')
	pdf.cell(45,5,'Data', 1,0,'C')
	pdf.cell(90,5,'Valor', 1,1,'C')
	pdf.cell(10,5,'', 1,0,'C')
	pdf.cell(25,5,'', 1,0,'C')
	pdf.cell(55,5,'', 1,0,'C')
	pdf.cell(45,5,'', 1,0,'C')
	pdf.cell(45,5,'', 1,0,'C')
	pdf.cell(90,5,'', 1,1,'C')
	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado

@app.route('/api/grafico', methods=['GET'])
def gerar_grafico():
	class PDF(FPDF):
		def header(self):
			self.set_font('Arial','', 8)
	pdf = PDF()
	pdf.add_page('L')
	pdf.set_font('Arial','B',10)
	pdf.multi_cell(270,5,'4.1.1 EVOLUÇÃO DA ARRECADAÇÃO DO FUNDO DE DESENVOLVIMENTO SUSTENTÁVEL - FDS',align='J')
	pdf.multi_cell(90,15,'Valor total Bruto Recolhido ao\nFDS (R$*)', 1,1,'C')
	pdf.set_font('Arial','B',8)
	pdf.cell(45,5,'Período', 1,0,'C')
	pdf.cell(45,5,'Valor (R$)', 1,1,'C')
	pdf.set_font('Arial','',8)
	pdf.cell(45,5,'2003', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2004', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2005', 1,0,'C')
	pdf.cell(45,5,'28,56', 1,1,'C')
	pdf.cell(45,5,'2006', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2007', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2008', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2009', 1,0,'C')
	pdf.cell(45,5,'28,56', 1,1,'C')
	pdf.cell(45,5,'2010', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2011', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2012', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.cell(45,5,'2013', 1,0,'C')
	pdf.cell(45,5,'313,2', 1,1,'C')
	pdf.cell(45,5,'2014', 1,0,'C')
	pdf.cell(45,5,'721,12', 1,1,'C')
	pdf.cell(45,5,'2015', 1,0,'C')
	pdf.cell(45,5,'-', 1,1,'C')
	pdf.set_font('Arial','B',8)
	pdf.cell(45,5,'TOTAL', 1,0,'C')
	pdf.cell(45,5,'1.091,26', 1,1,'C')
	fn = 'download.pdf'
	pdfgerado = make_response(u''.join(pdf.output(fn,dest='S')).encode('latin-1'))
	pdfgerado.headers.set('Content-Disposition', 'attachment', filename=fn)
	pdfgerado.headers.set('Content-Type', 'application/pdf')
	return pdfgerado