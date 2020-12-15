#include "lists.h"
#include <stdio.h>

int is_palindrome(listint_t **head)
{

        /**
         * 1. Revisar si head existe -ok
         * 2. Crear buffer -ok
         * 3. Crear var length_buffer -ok
         * 4. Recorrer linked -ok
         * 4.1 Aumento length_buffer -ok
         * 4.2 Paso dato de nodo->n a buffer[length_buffer] -ok
         * 4.3 Cuando nodo->next == NULL cierro el buffer con \0 -ok
         * 5. Recorro el buffer en las dos direcciones hasta
         *    que left >= rigth
         * 5.2 Comparo datos, si no son iguales NOT_PALINDROME
         *     si son iguales IS_PALINDROME
         */

        if (*head && (*head)->next)
        {
                int buffer[1024 * 10];
                int length = 0;
                int left = 0;
                int right = 0;
                listint_t *temp = NULL;

                temp = *head;
                while (temp)
                {
                        buffer[length] = temp->n;
                        length++;
                        temp = temp->next;
                }
                buffer[length] = '\0';
                right = length - 1;
                for (; left <= right; left++, right--)
                {
                        if (buffer[left] != buffer[right])
                                return (NOT_PALINDROME);
                }
                return (IS_PALINDROME);
        }
        else
                return (IS_PALINDROME);
}