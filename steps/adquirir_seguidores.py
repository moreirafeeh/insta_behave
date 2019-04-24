@given(u'Pagina inicial do instagram')
def step_impl(context):
    context.instagram.ir_ate_o_seguidor_escolhido('bielzau')
    pass


@when(u'procurar por seguidor base')
def step_impl(context):
    context.instagram.seguir()
    pass


@then(u'Comecar a seguir')
def step_impl(context):
    pass