from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
#первый отправляет, затем получает (не получилось через comm.sendrecv)
if rank == 0:
    for i in range(1, 6):
        message = i
        print("-1- I AM FIRST WISER : ", message)
        comm.send(message, dest=1)
        rec_message = comm.recv(source=1)
        if rec_message % 2 == 0:
            print("second said: Message N ", rec_message)
else:
#второй получает, затем отправляет
    for i in range(1, 6):
        rec_message = comm.recv(source=0)
        if rec_message % 2 == 0:
            print("first said : Message N ", rec_message)
        send_message = i
        print("-2- I AM SECOND WISER : ", send_message)
        comm.send(send_message, dest=0)

MPI.Finalize()
