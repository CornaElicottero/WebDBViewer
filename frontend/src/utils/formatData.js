export const formatData = (jsonData) =>{
    let arrayOfJson = []
    if (jsonData.length > 0){
    for (const item of jsonData){
        let formatJSON = {}
        if (item?.codecId !== undefined){
            let key = 'Идентификатор кодека'
            formatJSON[key] = item?.codecId
        }
        if (item?.model?.modelId !== undefined){
            let key = 'Идентификатор модели'
            formatJSON[key] = item?.model?.modelId
        }
        if (item?.model?.modelName !== undefined){
            let key = 'Название модели'
            formatJSON[key] = item?.model?.modelName
        }
        if (item?.model?.manufacturerId?.manufacturerId !== undefined){
            let key = 'Идентификатор производителя'
            formatJSON[key] = item.model?.manufacturerId?.manufacturerId
        }
        if (item?.model?.manufacturerId?.manufacturerName !== undefined){
            let key = 'Название производителя'
            formatJSON[key] = item.model?.manufacturerId?.manufacturerName
        }
        if (item?.serialNumber !== undefined){
            let key = 'Серийный номер'
            formatJSON[key] = item?.serialNumber
        }
        if (item?.inventoryNumber !== undefined){
            let key = 'Инвентарный номер'
            formatJSON[key] = item?.inventoryNumber
        }
        if (item?.startYear !== undefined){
            let key = 'Год введения в эксплуатацию'
            formatJSON[key] = item?.startYear
        }
        if (item?.division?.divisionId !== undefined){
            let key = 'Идентификатор подразделения'
            formatJSON[key] = item?.division?.divisionId
        }
        if (item?.division?.divisionCode !== undefined){
            let key = 'Код подразделения'
            formatJSON[key] = item?.division?.divisionCode
        }
        if (item?.division?.divisionMidName !== undefined){
            let key = 'Структурное подразделение'
            formatJSON[key] = item?.division?.divisionMidName
        }
        if (item?.division?.divisionMinName !== undefined){
            let key = 'Сокращ. структурное подразделение'
            formatJSON[key] = item?.division?.divisionMinName
        }
        if (item?.division?.divisionFullName !== undefined){
            let key = 'Полное структурное подразделение'
            formatJSON[key] = item?.division?.divisionFullName
        }
        if (item?.location?.localityId !== undefined){
            let key = 'Идентификатор местонахождения'
            formatJSON[key] = item?.location?.localityId
        }
        if (item?.location?.localityName !== undefined){
            let key = 'Местонахождение'
            formatJSON[key] = item?.location?.localityName
        }
        if (item?.street?.streetId !== undefined){
            let key = 'Идентификатор улицы'
            formatJSON[key] = item?.street?.streetId
        }
        if (item?.street?.streetName !== undefined){
            let key = 'Улица'
            formatJSON[key] = item?.street?.streetName
        }
        if (item?.room !== undefined){
            let key = '№ помещения'
            formatJSON[key] = item?.room
        }
        if (item?.usedBy?.subdivisionId !== undefined){
            let key = 'Идентификатор кем используется'
            formatJSON[key] = item?.usedBy?.subdivisionId
        }
        if (item?.usedBy?.subdivisionName !== undefined){
            let key = 'Кем используется'
            formatJSON[key] = item?.usedBy?.subdivisionName
        }
        if (item?.e164 !== undefined){
            let key = 'e164'
            formatJSON[key] = item?.e164
        }
        if (item?.h323id !== undefined){
            let key = 'h323id'
            formatJSON[key] = item?.h323id
        }
        if (item?.onService !== undefined){
            let key = 'На ремонте'
            formatJSON[key] = item?.onService
        }
        if (item?.ip !== undefined){
            let key = 'IP-адрес'
            formatJSON[key] = item?.ip
        }
        if (item?.mask?.maskId !== undefined){
            let key = 'Идентификатор маски'
            formatJSON[key] = item?.mask?.maskId
        }
        if (item?.mask?.mask !== undefined){
            let key = 'Маска'
            formatJSON[key] = item?.mask?.mask
        }
        if (item?.gateway !== undefined){
            let key = 'Gateway'
            formatJSON[key] = item?.gateway
        }
        if (item?.buildingNumber !== undefined){
            let key = '№ здания'
            formatJSON[key] = item?.buildingNumber
        }
        if (item?.spisan !== undefined){
            let key = 'Списан'
            formatJSON[key] = item?.spisan
        }
        arrayOfJson.push(formatJSON)
    }
    return arrayOfJson
    }
}
