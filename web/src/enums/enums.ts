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

/**
 * @description: 开户选择的交易能力
 */
const BrokerOpenAbility = {
    BY: [Ability.US_STOCK, Ability.JP_STOCK, Ability.FUTURES, Ability.CRYPTO],
    CG: [Ability.SG_STOCK, Ability.UK_STOCK, Ability.FOREX],
    CR: [Ability.HK_STOCK, Ability.A_STOCK, Ability.FUND, Ability.BOND],
    US: [Ability.US_STOCK, Ability.OPTION, Ability.FOREX, Ability.CRYPTO, Ability.DE_STOCK],
    JP: [Ability.JP_STOCK, Ability.US_STOCK],
    HK: [Ability.HK_STOCK, Ability.A_STOCK, Ability.FUND, Ability.FUTURES],
};

/**
 * @description: 激活选择的交易能力
 */
const BrokerActivateAbility = {
    BY: [Ability.UK_STOCK, Ability.A_STOCK, Ability.FUND, Ability.DE_STOCK],
    CG: [Ability.US_STOCK, Ability.FOREX, Ability.CRYPTO, Ability.FUND],
    CR: [Ability.JP_STOCK, Ability.US_STOCK],
    US: [Ability.SG_STOCK, Ability.A_STOCK, Ability.CRYPTO],
    JP: [Ability.A_STOCK, Ability.FUND, Ability.BOND, Ability.OPTION],
    HK: [Ability.US_STOCK, Ability.JP_STOCK, Ability.UK_STOCK, Ability.SG_STOCK],
}

/**
 * @description: 个人户/机构户
 */
const enum Kind {
    individual = "个人",
    institution = "机构",
}

/**
 * @description: 账户融资类型
 */
const enum Type {
    margin = "融资",
    cash = "现金",
}

/**
 * @description: 账户种类枚举
 */
const enum Model {
    fund_acc = "基金账户",
    single_acc = "单一账户",
    uni_acc = "统一账户",
}

/**
 * @description: 账户开通状态
 */
const enum Status {
    closed = "已关闭",
    opened = "已开通",
}

export {Broker, Attribution, Ability, Kind, Type, Model, Status, BrokerOpenAbility, BrokerActivateAbility};
