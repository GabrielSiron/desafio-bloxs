import { Header, Page, MenuItem, Text,
    Logo, AmountCard, Line, TitleCard, TransactionsContainer,
    AmountValue, DepositButton, DraftButton, TransactionsList } from './style';

import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';

import { UserContext } from '../../contexts/user';
import { useState, useContext, useEffect } from 'react';
import { Get, GetFirstPage } from '../../services/crud';
import Transaction from '../../components/Transaction/index';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const { email, password, name, cpf, token, setToken, setEmail, setPassword } = useContext(UserContext);

    const [loading, setLoading] = useState(false);
    const [account, setAccount] = useState({message: '', amount: 0, name: ''});
    const [transactions, setTransactions] = useState([])
    
    let navigate = useNavigate();

    const Logout = () => {
        sessionStorage.removeItem('token');   
        setToken('')
        navigate('/signin')
    }

    useEffect(() => {

        let token = sessionStorage.getItem('token') || ''
        
        if(token.length == 0){
            navigate('/signin')
        }

        const GetAccountInfo = async () => {
            let token = sessionStorage.getItem('token') || '';
            await Get('account', token, setAccount);
            
        }

        const GetTransactions = async () => {
            let token = sessionStorage.getItem('token') || '';
            GetFirstPage('transactions', '1', token, setTransactions)
        }

        GetTransactions()
        GetAccountInfo()
        
    }, [])

    return(
        <Page>
            <Header>
                <Logo src={LogoTotal}/>
                <MenuItem onClick={Logout}>
                    <Text>Sair</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Sobre</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Transações</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Menu</Text>
                </MenuItem>
            </Header>
            <Line>
                <AmountCard>
                    <TitleCard>Saldo</TitleCard>
                    <AmountValue>{ 'R$ ' + account.amount }</AmountValue>
                </AmountCard>
                <DepositButton type='button'>Depositar</DepositButton>
                <DraftButton type='button'>Sacar</DraftButton>
            </Line>
            <Line>
                <TransactionsContainer>
                    <TitleCard>Transações</TitleCard>
                    <TransactionsList>
                        {
                            transactions.map((transaction, i) => <Transaction transaction={transaction}></Transaction>)
                        }
                    </TransactionsList>
                </TransactionsContainer>
            </Line>
        </Page>
    )
}

export default Home;