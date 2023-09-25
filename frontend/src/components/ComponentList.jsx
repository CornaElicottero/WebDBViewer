import React from 'react';

function ComponentList({ jsonData }) {
    const labels = [
        'Структурное подразделение',
        'Орг. ед.',
        'Производитель',
        'Модель',
        'Серийный номер',
        'Инвентарный номер',
        'IP-адрес',
        'Маска',
        'GW'
    ];


    return (
        <div className={'wrapper'}>
            {labels.map((label, index) => (
                <>
                    <div key={index} className={"list_item_left"}>{label}</div>
                    <div key={labels.length+index} className={"list_item_right"}>{jsonData[label]}</div>
                </>
                ))}
        </div>
    )
}
export default ComponentList;
