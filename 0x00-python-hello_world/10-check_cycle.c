/**
 * functions allowed
 * write, printf, putchar, puts, malloc, free
 */

#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to head of the list
 * Description: This function uses Floyd's Hare and Tortoise algorithm 
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    int cycle = 0;
    listint_t *turtoise = list;
    listint_t *hare = list;

    if (list == NULL)
        return (cycle);

    while (hare->next->next != NULL)
    {
        hare = hare->next->next;
        turtoise = turtoise->next;
        if (hare == turtoise)
        {
            cycle = 1;
            break;
        }
    }

    return (cycle);
}