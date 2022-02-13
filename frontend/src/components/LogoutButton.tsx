import React from "react";
import { Stack, Button } from "@chakra-ui/react";
import { useAuth0 } from "@auth0/auth0-react";

interface LogoutButtonProps {
    ml: string
}

export const LogoutButton = ({ml}: LogoutButtonProps) => {
    const { logout } = useAuth0()

    return (
        <Stack direction="row" spacing={4} align="center">
            <Button
            loadingText="Loading"
            colorScheme="black"
            variant="outline"
            spinnerPlacement="start"
            onClick={() => logout({returnTo: window.location.origin})}
            ml={ml}
            >
            Log Out
            </Button>
        </Stack>
    )
};
