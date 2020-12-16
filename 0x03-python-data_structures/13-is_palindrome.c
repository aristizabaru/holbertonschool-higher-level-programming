#include "lists.h"
#include <stdio.h>

int is_palindrome(listint_t **head)
{
        if (*head && (*head)->next)
        {
                int buffer[1024 * 5];
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