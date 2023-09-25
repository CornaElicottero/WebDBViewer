import React, { useState } from 'react';

function Form({ jsonData }) {
    const labels = [
        'Производитель',
        'Модель',
        'Серийный номер',
        'Инвентарный номер',
        'Год введения в эксплуатацию',
        'Структурное подразделение',
        'Местонахождение',
        'Улица',
        '№ здания',
        '№ помещения',
        'Кем используется',
        'e164',
        'h323id',
        'IP-адрес',
        'Маска',
        'GW',
        'На ремонте',
        'Списан'
    ];

    const [inputValues, setInputValues] = useState({});

    const handleChange = (label, value) => {
        setInputValues((prevValues) => ({
            ...prevValues,
            [label]: value
        }));
    };

    const handleSubmit = () => {
        const generatedJsonData = labels.reduce((jsonObj, label) => {
            jsonObj[label] = inputValues[label] || '';
            return jsonObj;
        }, {});

        const jsonString = JSON.stringify(generatedJsonData, null, 2);

        const blob = new Blob([jsonString], { type: 'application/json' });

        const anchor = document.createElement('a');
        anchor.href = URL.createObjectURL(blob);
        anchor.download = 'generatedData.json';
        anchor.click();
    };

    return (
        <>
        <div className={'wrapper'}>
            {labels.map((label, index) => {
                if (label === 'На ремонте' || label === 'Списан') {
                    return (
                        <React.Fragment key={index}>
                            <div className={'list_item_left'}>{label}</div>
                            <select
                                className={'list_item_right_input'}
                                value={inputValues[label] || ''}
                                onChange={(e) => handleChange(label, e.target.value)}
                            >
                                <option className={'select_option'} value="" disabled hidden>Выберите</option>
                                <option value="Да">Да</option>
                                <option value="Нет">Нет</option>
                            </select>
                        </React.Fragment>
                    );
                } else {
                    return (
                        <React.Fragment key={index}>
                            <div className={'list_item_left'}>{label}</div>
                            <input
                                type="text"
                                className={'list_item_right_input'}
                                value={inputValues[label] || ''}
                                onChange={(e) => handleChange(label, e.target.value)}
                            />
                        </React.Fragment>
                    );
                }
            })}

        </div>
    <button className={'btn'} onClick={handleSubmit}>Сохранить</button>
        </>
    );
}

export default Form;
