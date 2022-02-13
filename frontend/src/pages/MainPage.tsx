import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'
import { Center } from '@chakra-ui/react'

interface MainPageProps {
    isLoggedIn?: boolean
}

export const MainPage = ({isLoggedIn}: MainPageProps) => {
    const { user } = useAuth0()

    return (
        <Center>
            <div>Hello, {user?.given_name}</div>
        </Center>
    )
}