from metaflow import FlowSpec, step

class AttendingClassesFlow(FlowSpec):

    @step
    def start(self):
        self.name = "Apriyanto"
        print(f"Memulai proses mengikuti kuliah informatika untuk {self.name}.")
        self.next(self.pay_tuition)

    @step
    def pay_tuition(self):
        pembayaran = True
        if pembayaran == True:
            self.tuition_paid = True
            print("Biaya SPP telah dibayar.")
        else:
            self.tuition_paid = False
            print("Biaya SPP belum dibayar.")
        self.next(self.attend_lectures)

    @step
    def attend_lectures(self):
        if not self.tuition_paid:
            print("Tidak dapat mengikuti kuliah tanpa membayar biaya SPP.")
            return
        print(f"{self.name} sedang mengikuti kuliah...")
        self.next(self.submit_assignments)

    @step
    def submit_assignments(self):
        print("Mengumpulkan tugas...")
        self.next(self.take_exams)

    @step
    def take_exams(self):
        print("Mengikuti ujian...")
        self.next(self.receive_grades)

    @step
    def receive_grades(self):
        print("Menerima nilai...")
        self.final_grade = "A"  # Simulasi perhitungan nilai
        print(f"Nilai akhir {self.name} diterima: {self.final_grade}")
        self.next(self.end)

    @step
    def end(self):
        print("Proses selesai.")

if __name__ == '__main__':
    AttendingClassesFlow()

