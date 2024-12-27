import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

def random_email():
    return fake.email()

def random_uf():
    ufs = [
        'AC', 
        'AL', 
        'AP', 
        'AM', 
        'BA', 
        'CE', 
        'DF', 
        'ES', 
        'GO', 
        'MA', 
        'MT', 
        'MS', 
        'MG', 
        'PA', 
        'PB', 
        'PR', 
        'PE', 
        'PI', 
        'RJ', 
        'RN', 
        'RS', 
        'RO', 
        'RR', 
        'SC', 
        'SP', 
        'SE', 
        'TO'
        ]
    return random.choice(ufs)

def random_department():
    departments = [
        'Backoffice Operacional',
        'CDC (Varejo)',
        'Central de Relacionamento (SAC)',
        'Controladoria/Compras/Adm.Infraestrutura/Implantação',
        'Convênio Consignado Privado Comercial',
        'Corban (distribuidores)/Atendimento Remoto',
        'Departamento Pessoal',
        'Diretamente ligado à Diretoria ou Superintendência',
        'Financeiro',
        'Inteligência de negócios/Dados e Analytics',
        'Jurídico/Compliance',
        'Loja/Marketplace',
        'Marketing (Mídias/Marca/Trade)',
        'Mesa de Crédito/Mesa de Análise/Prevenção a Fraude e Backoffice',
        'Monitoria de Qualidade',
        'Pessoas e Cultura',
        'Planejamento Comercial/Pricing/Negócios Cias (Energia)',
        'Política de Crédito e Modelos/Monitoramento',
        'Produtos (Empréstimos/Financiamentos/Débito em Conta/Novos Negócios/Consignado Privado/Produtos Digitais)',
        'Recuperação de Crédito (Cobrança)',
        'Sucesso do Cliente',
        'Sucesso do Parceiro/Desenvolvimento de Canais/Apoio/Credenciamento',
        'Televendas Londrina',
        'Televendas Maringá',
        'TI (Infra e Operações/Core Financeiro/Corporativo/Originação)'
        ]
    return random.choice(departments)

def random_contract_type():
    contract_types = [
        'CLT',
        'PJ'
        ]
    return random.choice(contract_types)

def random_age_group():
    age_groups = [
        'Até 25 anos', 
        'De 26 a 34 anos', 
        'De 35 a 44 anos', 
        'De 45 a 54 anos', 
        '55 anos ou mais'
        ]
    return random.choice(age_groups)

def random_gender():
    genders = [
        'Masculino', 
        'Feminino', 
        'Outro'
        ]
    return random.choice(genders)

def random_service_time():
    service_times = [
        'Até 1 ano', 
        'Entre 1 e 2 anos', 
        'Entre 3 e 5 anos', 
        'Entre 6 e 10 anos', 
        '11 anos ou mais'
        ]
    return random.choice(service_times)

def random_education():
    educations = [
        'Ensino médio completo ou menos', 
        'Ensino superior em andamento', 
        'Ensino superior completo', 
        'Pós-graduação em andamento ou completo'
        ]
    return random.choice(educations)

def random_agreement():
    agreements = [
        "Concordo totalmente",
        "Concordo Parcialmente",
        "Não concordo e nem discordo",
        "Discordo parcialmente",
        "Discordo totalmente"
    ]
    return random.choice(agreements)

data = {
    'Hora de início': [fake.date_time_this_year() for _ in range(1000)],
    'Hora de conclusão': [fake.date_time_this_year() for _ in range(1000)],
    'Email': [random_email() for _ in range(1000)],
    'Nome': [fake.name() for _ in range(1000)],
    'UF': [random_uf() for _ in range(1000)],
    'DEPARTAMENTO': [random_department() for _ in range(1000)],
    'TIPO DE CONTRATO': [random_contract_type() for _ in range(1000)],
    'FAIXA ETÁRIA': [random_age_group() for _ in range(1000)],
    'GÊNERO': [random_gender() for _ in range(1000)],
    'TEMPO DE CASA': [random_service_time() for _ in range(1000)],
    'ESCOLARIDADE': [random_education() for _ in range(1000)],
}

questions = [
    "As comunicações institucionais são claras e objetivas",
    "Meu líder me mantem informado sobre assuntos importantes e mudança organizacionais",
    "Entendo as metas e as estratégias da empresa para alcançar seus objetivos",
    "Sei do meu papel e como contribuir dentro da estratégia da empresa e entendo os resultados esperados por essa contribuição",
    "A comunicação entre os diferentes times é clara e objetiva",
    "Sinto-me confortável para tirar dúvidas e propor soluções",
    "Meu líder transmite segurança na tomada de decisões",
    "Meu lider trata de forma justa e igualitária todos os colaboradores",
    "O meu líder seleciona pessoas cujas virtudes se enquadram bem aqui",
    "O meu líder sabe coordenar pessoas e distribuir tarefas adequadamente",
    "O meu líder tem uma visão clara de para onde estamos indo e como fazer para chegar lá.",
    "O meu líder cumpre o que promete",
    "Meu líder age de acordo com o que fala, demonstrando transparência em suas ações",
    "Os conflitos dentro do time são tratados de forma adequada",
    "Se cometemos um erro somos incentivados a falar sobre o assunto para solucionar o problema",
    "Os treinamentos que recebo me capacitam a fazer bem o meu trabalho",
    "Meu líder me dá bons feedbacks sobre como posso melhorar meu desempenho e reconhece quando faço um bom trabalho",
    "A empresa reconhece frequentemente os colaboradores",
    "O espaço físico é adequado ao meu trabalho",
    "O meu líder incentiva a participação do time na tomada de decisões",
    "Meu líder é receptivo às críticas e feedbacks",
    "Acredito que estamos em um ambiente de companheirismo, respeito e empatia para que todos possam dar o seu melhor",
    "Não tenho barreiras ou dificuldades para acessar e trabalhar com outros times",
    "Aqui as pessoas se importam umas com as outras e existe cooperação mútua",
    "Temos benefícios adequados em relação à maioria das outras empresas",
    "A empresa se preocupa e investe em ações de desenvolvimento para os colaboradores",
    "Nossas instalações contribuem para um bom ambiente de trabalho",
    "Me sinto valorizado pela empresa",
    "Acredito que estou tendo oportunidades semelhantes a profissionais que ocupam mesmo nível de função.",
    "Percebo que a empresa reconhece os bons colaboradores",
    "Sinto que sou considerado importante, independente da posição que ocupo",
    "Tenho confiança de que as promoções são para pessoas que realmente merecem",
    "Meu líder evita o favoritismo",
    "Percebo que aqui as pessoas evitam fazer 'politicagem' e intrigas como forma de serem favorecidas",
    "Tenho certeza de que se mostrar um bom trabalho, serei reconhecido por ele",
    "As pessoas que trabalham aqui são bem tratadas independente da idade, sexo, orientação sexual, crenças, raça, cor, dentre outros",
    "Caso eu seja tratado injustamente, acredito que serei ouvido e que serei orientado corretamente",
    "Sei onde devo recorrer caso presencie ou seja vítima de uma situação injusta",
    "Percebo que todos os nossos colaboradores tem o mesmo valor, pois cada um contribui de alguma forma para o sucesso da empresa",
    "O meu trabalho me dá um sentimento de realização profissional",
    "Tenho orgulho do trabalho que eu realizo",
    "Considero que minhas competências técnicas e comportamentais têm sido bem aproveitadas em meu cargo atual",
    "Percebo que sou desafiado em minhas atividades",
    "Percebo que todos em meu time são colaborativos da mesma forma",
    "Quando vejo o que fazemos em meu time, sinto orgulho",
    "Percebo que um time tem confiança no trabalho de outros times, não havendo interferências nem questionamentos em excesso",
    "Percebo que meu time coopera com o trabalho de outros times de trabalho",
    "Os assuntos importantes são debatidos em conjunto",
    "A Empresa X é uma empresa ética com seus colaboradores/clientes/parceiros",
    "Eu já indiquei um amigo para trabalhar na Empresa X",
    "Tenho orgulho de trabalhar na Empresa X",
    "Pretendo trabalhar aqui por muito tempo",
    "A experiência de trabalhar na Empresa X possibilita a criação de amizades fora do ambiente de trabalho",
    "Sempre comemoramos eventos especiais",
    "As pessoas podem ser autênticas na empresa, expressando sua personalidade sem receio",
    "Caso alguem esteja com algum problema pessoal ou lutando por uma causa, as pessoas aqui tendem a colaborar",
    "Sinto facilidade de me integrar com colaboradores de outras áreas",
    "Quando chega um novo colaborador, as pessoas o acolhem rapidamente, fazendo-o se sentir bem vindo",
    "Os colaboradores que mudam de função conseguem se adaptar com rapidez, pois as pessoas são receptivas",
    "O programa de integração da Empresa X favorece o acolhimento das pessoas",
    "Existe um sentimento de 'família' na Empresa X",
    "As pessoas aqui tendem a ser humildes, pensando coletivamente e não somente nos interesses pessoais",
    "A Empresa X valoriza o espírito de sustentabilidade (meio ambiente, econômico e social)",
    "As áreas colaboram umas com as outras, mesmo que tenham que fazer sacrifícios, pensando no que é melhor para a empresa",
    "Eu recomendaria a Empresa X para alguém que esteja buscando uma oportunidade de trabalho",
    "Nós já avaliamos sua liderança direta. Você tem algum comentário sobre algum líder que não esteja diretamente ligado à você?",
    "Você tem alguma ideia de ação que possa melhorar o clima e aumentar a satisfação dos colaboradores?"
]

for question in questions:
    data[question] = [random_agreement() for _ in range(1000)]

df = pd.DataFrame(data)
df.to_csv('data_faker.csv', index=False)
print("Arquivo criado com sucesso!")