from django.db import models


class Terminal(models.Model):

    name = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = "Terminal"
        verbose_name_plural = "Terminals"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Terminal_detail", kwargs={"pk": self.pk})


class MeasuredData(models.Model):

    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    temperature = models.FloatField()
    pressure = models.FloatField()

    class Meta:
        verbose_name = "Measured Data"
        verbose_name_plural = "Measured Data"

    def __str__(self):
        return f"{self.terminal.name}: {self.temperature} C, {self.pressure} mPa"

    def get_absolute_url(self):
        return reverse("MeasuredData_detail", kwargs={"pk": self.pk})
