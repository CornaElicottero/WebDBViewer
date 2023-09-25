const BACKEND_URL = process.env.REACT_APP_BACKEND_URL

export const getQuery = async (queryUniversal) => {
    try {
        let response = await fetch(BACKEND_URL + '/graphql',
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    query: `{
                              vcsSystems(vcsSystemsUniversal: "${queryUniversal}"){
                                codecId
                                model{
                                  modelId
                                  modelName
                                  manufacturerId{
                                    manufacturerId
                                    manufacturerName
                                  }
                                }
                                serialNumber
                                inventoryNumber
                                startYear
                                division{
                                  divisionId
                                  divisionCode
                                  divisionMidName
                                  divisionMinName
                                  divisionFullName
                                }
                                location{
                                  localityId
                                  localityName
                                }
                                street{
                                  streetId
                                  streetName
                                }
                                room
                                usedBy{
                                  subdivisionId
                                  subdivisionName
                                }
                                e164
                                h323id
                                onService
                                ip
                                mask{
                                  maskId
                                  mask
                                }
                                gateway
                                buildingNumber
                                spisan
                              }
                            }`
                })
            })
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Ошибка при получении данных:', error);
    }
}
