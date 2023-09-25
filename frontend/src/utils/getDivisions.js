const BACKEND_URL = process.env.REACT_APP_BACKEND_URL

export const getDivisions = async (queryUniversal) => {
    try {
        let response = await fetch(BACKEND_URL + '/graphql',
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    query: `{
                              divisions{
                                divisionId
                                divisionCode
                                divisionMidName
                                divisionMinName
                                divisionFullName
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
