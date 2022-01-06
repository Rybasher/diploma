signup_responses = {
    200: {
        "content": {
            "application/json": {
                "example": {"session_id": "18cb0578-f7cc-492a-b254-8e602e9ad541"}
            }
        },
        "description": "Return created user email and session id",
    },
    409: {
        "content": {
            "application/json": {
                "example": {"detail": "User exists"}
            }
        },
        "description": "Return exists error",
    }
}

signin_responses = {
    200: {
        "content": {
            "application/json": {
                "example": {"session_id": "18cb0578-f7cc-492a-b254-8e602e9ad541"}
            }
        },
        "description": "Returns the session id of the user",
    },
    401: {
        "content": {
            "application/json": {
                "example": {"detail": "Unauthorized"},
            }
        },
        "description": "Invalid credentials",
    }
}

forgot_password_responses = {
    200: {
        "content": {
            "application/json": {
                "example": {"null"}
            }
        },
        "description": "Email sent successfully",
    },
    401: {
        "content": {
            "application/json": {
                "example": {"detail": "User does not exist"}
            }
        },
        "description": "User with provided email not exist",
    }
}

reset_pass_responses = {
    200: {
        "content": {
            "application/json": {
                "example": {"Password updated successfully"}
            }
        },
        "description": "Password updated successfully",
    },
    400: {
        "content": {
            "application/json": {
                "example": {"detail": "Invalid token"}
            }
        },
        "description": "Invalid token",
    }
}

get_user_response = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "email": "hello@gmail.com",
                    "password": "testpassword",
                    "firstName": "James",
                    "lastName": "Cameron",
                    "phone": "180009455884",
                    "dateOfBirth": "2003-10-10",
                    "incidents": 1,
                    "oftenTravels": 0,
                    "createdAt": "2021-10-04T14:02:06.451014",
                    "stripeUserData": {
                        "id": "tok_lpc92x5ke4",
                        "usemode": False,
                        "card": {
                            "country": "PL",
                            "object": "card",
                            "brand": "Visa",
                            "last4": "4747",
                            "exp_month": 2,
                            "exp_year": 2030
                        }
                    },
                }
            }
        },
        "description": "Received user",
    },
    404: {
        "content": {
            "application/json": {
                "example": {"detail": "User does not exists"}
            }
        },
        "description": "User not found",
    }

}

check_user_exists_response = {
    200: {
        "content": {
            "application/json": {
                "example": {"detail": True}
            }
        },
        "description": "User found",
    },
    404: {
        "content": {
            "application/json": {
                "example": {"detail": False}
            }
        },
        "description": "User not found",
    }
}

refund_response = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "id": "re_3JfRv9KiyzTlxs5N0GTIX7ul",
                    "object": "refund",
                    "amount": 499,
                    "balance_transaction": "txn_3JfRv9KiyzTlxs5N0O8jHKLr",
                    "charge": "ch_3Jec01KiyzTlxs5N0eEO9hHy",
                    "created": 1633018625,
                    "currency": "usd",
                    "metadata": {},
                    "payment_intent": "pi_3JfRv9KiyzTlxs5N0kqcs9q3",
                    "reason": "null",
                    "receipt_number": "null",
                    "source_transfer_reversal": "null",
                    "status": "succeeded",
                    "transfer_reversal": "null"
                }
            }
        },
        "description": "Retrieve refund successfully",
    },
    400: {
        "content": {
            "application/json": {
                "example": {"detail": "Invalid refund id"}
            }
        },
        "description": "Refund with provided id not found",
    }
}

customer_response = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "id": "cus_KLa2Vklnx57VGr",
                    "object": "customer",
                    "address": None,
                    "balance": 0,
                    "created": 1633360510,
                    "currency": "usd",
                    "default_source": "null",
                    "delinquent": False,
                    "description": "My First Test Customer (created for API docs)",
                    "discount": None,
                    "email": "",
                    "invoice_prefix": "4E24BE7",
                    "invoice_settings": {
                        "custom_fields": None,
                        "default_payment_method": None,
                        "footer": None
                    },
                    "livemode": False,
                    "metadata": {},
                    "name": None,
                    "next_invoice_sequence": 1,
                    "phone": None,
                    "preferred_locales": [],
                    "shipping": None,
                    "tax_exempt": "none"
                }
            }
        },
        "description": "Retrieve customer successfully",
    },
    400: {
        "content": {
            "application/json": {
                "example": {"detail": "Invalid customer id"}
            }
        },
        "description": "Customer with provided id not found",
    }
}

create_checkout_response = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "checkout_session_id": "cs_test_a1r7xzGWhySQvJWZvvbosVVpZLWsxK9cKG6yNp6mjvcgIWLZ6DUqT7bClH",
                    "checkout_public_key": "pk_test_51JeH2DKiyzTlxs514jixzwzrlBFcwBO2bar68MGLhcwZd6k9IjKrWsV2XCj4r2LtcjTvW3EOaYjzx725QhQ4KLLg00zNEPuA73",
                    "user": "pepam24528@busantei.com"
                }
            }
        },
        "description": "Successfully created checkout",
    },
}

create_support_ticket_response = {
    200: {
        "content": {
            "application/json": {
                "subject": "test",
                "describe": "test",
                "id": "187c0bd6-cedf-464c-a7e1-215872a3db52",
                "status": "open"
            }
        },
        "description": "Support ticket created successfully",
    },
    404: {
        "content": {
            "application/json": {
                "example": {"detail": "Ticket does not exists"}
            }
        },
        "description": "Ticket not found",
    },
    401: {
        "content": {
            "application/json": {
                "example": {"detail": "Unauthorized"},
            }
        },
        "description": "Invalid credentials",
    }
}

check_user_phone_exist = {
    401: {
            "content": {
                "application/json": {
                    "example": {"detail": "Unauthorized"},
                }
            },
            "description": "Invalid credentials",
        },

    409: {
            "content": {
                "application/json": {
                    "example": {"detail": "User exists"}
                }
            },
            "description": "Return exists error",
        }
}