from config import cfg
from yacs.config import get_cfg


if __name__ == "__main__":
    cfg.merge_from_file("config.yaml")
    cfg.freeze()

    cfg2 = cfg.clone()
    cfg2.defrost()
    cfg2.TRAIN.SCALES = (8, 16, 32)
    cfg2.freeze()
    cfg3 = get_cfg()
    print(f"cfg:\n-----\n{cfg} \n")
    print(f"cfg2:\n-----\n{cfg2} \n")
    print(f"cfg3:\n-----\n{cfg3} \n")
