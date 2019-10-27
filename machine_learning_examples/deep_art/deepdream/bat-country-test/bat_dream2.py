#!/usr/bin/env python 

""" Create dream 2 """ 

bc = BatCountry(args.base_model)
features = bc.prepare_guide(Image.open(args.guide_image), end=args.layer)
image = bc.dream(np.float32(Image.open(args.image)), end=args.layer,
    iter_n=20, objective_fn=BatCountry.guided_objective,
    objective_features=features,)
bc.cleanup()