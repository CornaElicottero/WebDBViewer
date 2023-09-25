import React, { useState } from 'react';

const Test = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const suggestionsList = ['Вариант 1', 'Вариант 2', 'Вариант 3'];

    const handleInputChange = (event) => {
        const { value } = event.target;
        setSearchQuery(value);
        const filteredSuggestions = suggestionsList.filter((suggestion) =>
            suggestion.toLowerCase().includes(value.toLowerCase())
        );

        setSuggestions(filteredSuggestions);
    };

    const handleSuggestionClick = (suggestion) => {
        setSearchQuery(suggestion);
        setSuggestions([]);
    };

    return (
        <div>
            <input
                className={"search_bar"}
                type="text"
                value={searchQuery}
                onChange={handleInputChange}
                placeholder="Поиск"
            />
            {suggestions.length > 0 && (
                <ul className="suggestions-list">
                    {suggestions.map((suggestion) => (
                        <li
                            key={suggestion}
                            className={"suggestion-item"}
                            onClick={() => handleSuggestionClick(suggestion)}
                        >
                            {suggestion}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Test;
