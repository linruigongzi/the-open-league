from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class JettonMintRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        jetton_masters = "\nor\n".join(map(lambda addr: f"jetton_master  = '{addr}'", metric.jetton_masters))

        return f"""
        select msg_id as id, '{context.project.name}' as project, 1 as weight, user_address, ts
        from jetton_mint_local
        WHERE {jetton_masters}
        """


"""
TEP-74 token (jetton) mint, i.e. transfer initiated by jetton master 
"""
class JettonMint(Metric):
    def __init__(self, description, jetton_masters=[]):
        assert type(jetton_masters) == list
        Metric.__init__(self, description, [JettonMintRedoubtImpl()])
        self.jetton_masters = jetton_masters

