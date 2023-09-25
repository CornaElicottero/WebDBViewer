import React, { useEffect, useState } from 'react';
import ComponentList from './ComponentList';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL

const ListItem = ({ searchPayload }) => {
    const [jsonData, setJsonData] = useState(null);
    useEffect(() => {
        const fetchData = async () => {
            try {
                let response = await fetch(BACKEND_URL + '/graphql',
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            query: `{
                                      vcsSystems(vcsSystemsUniversal: "${searchPayload}"){
                                        division{
                                          divisionFullName
                                        }
                                        usedBy{
                                          subdivisionName
                                        }
                                        model{
                                          manufacturerId{
                                            manufacturerName
                                          }
                                          modelName
                                        }
                                        serialNumber
                                        inventoryNumber
                                        ip
                                        mask{
                                          mask
                                        }   
                                        gateway
                                      }
                                    }`
                        })
                    })
                const data = await response.json();
                setJsonData(data);
            } catch (error) {
                console.error('Ошибка при получении данных:', error);
            }
        };

        fetchData();
    }, [searchPayload]);

    const transformData = (jsonData) => {
        if (jsonData.data.vcsSystems.length > 0){
            const vcsSystems = jsonData.data.vcsSystems[0];
                return {
                    'Структурное подразделение': vcsSystems.division.divisionFullName,
                    'Орг. ед.': vcsSystems.usedBy.subdivisionName,
                    'Производитель': vcsSystems.model.manufacturerId.manufacturerName,
                    'Модель': vcsSystems.model.modelName,
                    'Серийный номер': vcsSystems.serialNumber,
                    'Инвентарный номер': vcsSystems.inventoryNumber,
                    'IP-адрес': vcsSystems.ip,
                    'Маска': vcsSystems.mask.mask,
                    'GW': vcsSystems.gateway
                }
        }
        else{
            return {
                'Структурное подразделение': 'Не найдено',
                'Орг. ед.': 'Не найдено',
                'Производитель': 'Не найдено',
                'Модель': 'Не найдено',
                'Серийный номер': 'Не найдено',
                'Инвентарный номер': 'Не найдено',
                'IP-адрес': 'Не найдено',
                'Маска': 'Не найдено',
                'GW': 'Не найдено'
            }
        }
    };

    return (
        <>
            {jsonData ? (
                <>
                <ComponentList  jsonData={transformData(jsonData)} />
                </>
                ) : (
                <div>Ожидание поискового запроса...</div>
            )}
        </>
    );
}

export default ListItem;
