/**
 * @description: 开户券商
 */
const enum Broker {
    BY = "BY券商",
    CG = "CG券商",
    CR = "CR券商",
    US = "US券商",
    JP = "JP券商",
    HK = "HK券商",
}

/**
 * @description: 归属地
 */
const enum Attribution {
    BY = "BY券商",
    CG = "CG券商",
    CR = "CR券商",
    US = "US券商",
    JP = "JP券商",
    HK = "HK券商",
}

/**
 * @description: 交易能力
 */
const enum Ability {
    US_STOCK = "美股",
    HK_STOCK = "港股",
    A_STOCK = "A股",
    JP_STOCK = "日股",
    SG_STOCK = "新股",
    UK_STOCK = "英股",
    DE_STOCK = "德股",
    FUND = "基金",
    BOND = "债券",
    FUTURES = "期货",
    OPTION = "期权",
    FOREX = "外汇",
    CRYPTO = "加密货币",
}

const enum BrokerOpenAbility {
    // HK = [Ability.HK_STOCK, Ability.A_STOCK],
}

const enum BrokerActivateAbility {

}

const enum Kind {
    individual = "个人",
    institution = "机构",
}

const enum Type {
    margin = "融资",
    cash = "现金",
}

const enum Model {
    fund_acc = "基金账户",
    single_acc = "单一账户",
    uni_acc = "统一账户",
}

const enum Status {
    closed = "已关闭",
    opened = "已开通",
}


export {Broker, Attribution, Ability, Kind, Type, Model, Status, BrokerOpenAbility, BrokerActivateAbility};
