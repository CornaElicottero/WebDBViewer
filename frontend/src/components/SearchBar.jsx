import React, {useState, useRef, useEffect} from "react";
import ComponentList from "./ComponentList";
import ListItem from "./ListItem";
import {getQuery} from "../utils/queryData";
import {formatData} from "../utils/formatData";

const SearchBar = ({ onChangeSearchPayload }) => {
    const searchPayload = useRef("");
    const [searchJSON, setSearchJSON] = useState([]);
    const [suggestions, setSuggestions] = useState([]);
    let timerId;
    const [searchQuery, setSearchQuery] = useState('');
    const handleSearchChange = (e) => {
        clearTimeout(timerId)
        setSearchQuery(e.target.value);
        searchPayload.current = e.target.value
        let foundIndexes = []
        let formatedJson= []
        let foundJson = []
        let foundValues = []
        if (searchPayload.current.length >= 3){
            timerId = setTimeout(async () => {
                getQuery(searchPayload.current)
                    .then(data => {
                        formatedJson = formatData(data?.data?.vcsSystems);
                    })
                    .then(() => {
                        for (const item of formatedJson) {
                            const jsonKeys = Object.keys(item)
                            const jsonValues = Object.values(item)
                            foundIndexes = jsonValues
                                .map((value, index) => ({ value, index }))
                                .filter(({ value }) => {
                                    return JSON.stringify(value).includes(searchPayload.current);
                                })
                                .map(({ index }) => index);
                            if (foundIndexes.length > 0) {
                                for (const foundIndex of foundIndexes){
                                    foundJson.push(item)
                                    foundValues.push([jsonKeys[foundIndex], jsonValues[foundIndex]])
                                }
                            }
                        }
                        if (foundJson.length > 0) {
                            setSuggestions(foundValues)
                            setSearchJSON(foundJson)
                        }
                    })
            })
        }
    }
    const handleSuggestionClick = (suggestion) => {

        setSuggestions([]);
    };
    return (
        <>
        <div className="dropdown-container">
            <input
                className={"search_bar"}
                type="text"
                value={searchQuery}
                onChange={handleSearchChange}
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
                            {suggestion[0] + ": " + suggestion[1]}
                        </li>
                    ))}
                </ul>
            )}
        </div>
        </>
    );
}


export default SearchBar
