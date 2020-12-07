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
    listint_t *turtoise, *hare;
    /* look if list is less than 2 nodes */
    if (list == NULL || list->next == NULL)
        return (cycle);
    /* assign initial position to hare and turtoise */
    hare = list->next->next;
    turtoise = list->next;

    while (hare->next->next)
    {
        if (hare == turtoise)
        {
            cycle = 1;
            break;
        }
        hare = hare->next->next;
        turtoise = turtoise->next;
    }

    return (cycle);
}