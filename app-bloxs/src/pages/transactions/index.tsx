import { useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { UserContext } from '../../contexts/user';
import { useState } from 'react';

import { Header, MenuItem, TitlePage, Page, Logo } from '../../styles/common-structure';
import { TransactionsCard, Line, TransactionsContainer, SeeMore } from './style';

import { GetFirstPage } from '../../services/crud';

import Transaction from '../../components/Transaction';

import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';

const Transactions = () => {
    const { setToken } = useContext(UserContext);

    const [transactions, setTransactions] = useState([])
    const [page, setPage] = useState(1)

    const GetTransactions = async (page: number) => {
        let token = sessionStorage.getItem('token') || '';
        GetFirstPage('transactions', page, token, setTransactions)
    }

    const GetNextPage = async () => {
        
        GetTransactions(page + 1);
        setPage(page + 1);
    }

    const SeeProfile = () => {
    
        navigate('/profile')
    }

    useEffect(() => {

        GetTransactions(1);

    }, [])

    let navigate = useNavigate();

    const Logout = () => {
        sessionStorage.removeItem('token');   
        setToken('');
        navigate('/');
    }

    const GoToHome = () => {
        navigate('/home');
    }

    return (
        <Page>
            <Header>
                <Logo src={LogoTotal} onClick={GoToHome}/>
                <MenuItem onClick={Logout}>
                    Sair
                </MenuItem>
                <MenuItem onClick={SeeProfile}>
                    Meu Perfil
                </MenuItem>
                <MenuItem>
                    Transações
                </MenuItem>
            </Header>
            <TitlePage>Transações Bancárias</TitlePage>
            <Line>
                <TransactionsCard>
                    <TransactionsContainer>
                        {
                            transactions.map((transaction, i) => <Transaction transaction={transaction}></Transaction>)
                        }
                        <SeeMore onClick={GetNextPage}>Carregar Mais</SeeMore>
                    </TransactionsContainer>
                </TransactionsCard>
            </Line>
            
        </Page>
    )
}

export default Transactions;