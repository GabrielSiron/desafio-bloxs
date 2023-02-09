export const GetById = async (endpoint: string, id: string, token: string, setItems: any) => {
    await fetch(`http://localhost:5000/${endpoint}/${id}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'token': token },
    })
    .then(async(resp)=>{
        let response = resp.json();
        setItems(response)
    });
}

export const GetFirstPage = async (endpoint: string, page: string, token: string, setItems: any) => {
    await fetch(`http://localhost:5000/${endpoint}/${page}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'token': token },
    })
    .then(async(resp)=>{
        let response = await resp.json();
        setItems(response[endpoint])
    });
}

export const Get = async (endpoint: string, token: string, setItems: any) => {
    await fetch(`http://localhost:5000/${endpoint}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'token': token },
    })
    .then(async(resp)=>{
        let response = await resp.json();
        console.log(response);
        
        setItems(response)
    });
}