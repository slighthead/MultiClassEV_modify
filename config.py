class Configuration:
    def __init__(self):
        self.data_dir= './preprocessed_data/'
        self.other_dir='../other'
        self.model='scibert'
        self.emb=100
        self.hid=100
        self.eval_batch_size=4
        self.lr=3e-5
        self.num_classes=2
        self.dropout=0.1
        self.cuda=True
        self.relation_weight=1.0
        self.entity_weight=1.0
        self.save_model=True
        self.load_model=False
        self.bert_config={}
        self.fine_tune=False
        self.eval_gold=True
        self.exp_id='test'
        self.random_seed=123
        self.output_dir='local_models/'
        self.nw_r=1.0
        self.nw_e=1.0
        self.regen_vocfile=False
        self.do_eval=False
        self.do_train=False
        self.do_test=True
        self.test_on_gold_tri=True
        self.kg_embedding_dim=300
        self.ent_linear_size=1000
        self.rel_linear_size=300
        self.use_knowledge=False
        self.use_temporal_edge=False
        self.link_pred=False
        self.nt_cls=False
        self.edge_cls=False
        self.mnc=False
        self.gpu=''
        self.gnn_type='ECGAT'
        self.local_rank=-1
        self.gradient_accumulation_steps=1
        self.warmup_proportion=0.1