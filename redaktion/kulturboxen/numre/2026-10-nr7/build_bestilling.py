import json, os
base = "/Users/lindau/codex/nyesider/redaktion/kulturboxen/numre/2026-10-nr7"
os.makedirs(base, exist_ok=True)

def opgave(slug, order, section, angle, words, mustCite, model, byline, fmt):
    return {
        "slug": slug, "order": order, "section": section,
        "brief": {"angle": angle, "words": words, "mustCite": mustCite,
                  "mustNumber": [], "format": fmt},
        "writer": {"byline": byline, "model": model, "fallback": None},
        "receipt": {"words": None, "costUSD": None, "draft": None},
        "verdict": {"status": None, "checkedAt": None, "citations": None, "editorNote": None},
    }

d = {
  "magazine": "kulturboxen",
  "issue": "2026-10-nr7",
  "issueTheme": "Slovenien - hverdag, arbejde, bolig, mad, penge, normer",
  "budget": {"articles": 7, "wordsPerArticle": [400, 680], "targetPages": 14,
             "note": "Kompakt som nr. 5 og nr. 6: ca. 7 artikler. Ikke 12-16."},
  "opgaver": [],
}

d["opgaver"].append(opgave("leder", 1, "Leder",
  "Editor-led. Slovenien som Europas stille barn: ikke feriebrochuren, men landet man bor i. Hverdag, arbejde, bolig, mad, penge, normer - uden at dømme, 150-350 ord.",
  [180, 350], 0, "editor-led", "", "leder"))

d["opgaver"].append(opgave("hverdagsspor", 2, "Hverdagsspor",
  "Feature: slovenske voksne flytter fra foraeldrene i gennemsnit som 29,1-aarige (Eurostat 2024, EU-snit 26,3; Danmark 21,8), og 59,1 % af 18-34-aarige bor stadig hos foraeldrene (SURS, 2023). Forklar hvorfor (boligpriser, familiepattern) og hvordan det maeles i hverdagen. Jeg skal have netop de to tal med fa knaaldende cite med year.",
  [420, 680], 2, "deepseek/deepseek-v3.2", "DeepSeek V3.2 (DeepSeek)", "feature"))

d["opgaver"].append(opgave("arbejde", 3, "Arbejde",
  "Feature: det slovenske arbejdsmarked. Beskaeftigelsesrater for 20-64-aarige: 78,3 % i 2025 mod 76,1 % i EU; arbejdosloshed 3,6 % mod 5,8 % i EU (Eurostat, 2025). Sloveniens faktiske arbejdsuge er 38,3 timer - 5. hoejeste i EU (EU i gennemsnit 35,9; Danmark 33,9 timer) (Eurostat, 2025). Forklar høj beskaeftighed + lang arbejdsuge. Brug netop disse tal med ar.",
  [420, 650], 2, "qwen/qwen3.7-max", "Qwen3.7 Max (Alibaba)", "feature"))

d["opgaver"].append(opgave("bolig", 4, "Bolig",
  "Feature: det slovenske boligmarked. 74,2 % ejer en bolig (Eurostat 2024, EU 68 %). Boligoverlastning kun 3,5 % af befolkningen mod EU-gennemsnit 7,7 % (Eurostat). Medianpriser 2024 (GURS/Banka Slovenije aarsrapport 2024, udgiven 2025): 2.920 EUR/kvm for en brugt lejlighed i hele landet, 4.510 EUR/kvm i Ljubljana, 2.330 EUR/kvm i Maribor. Boligpriser steg 8,5 % i 2024 (SURS HPI). Forklar seksuel kabevel at bruge netop disse tal.",
  [420, 680], 2, "mistralai/mistral-large", "Mistral Large (Mistral AI)", "feature"))

d["opgaver"].append(opgave("mad", 5, "Mad",
  "Feature: slovensk madkultur. Slovenska potica - EU TSG Midlertidigt Traditionel Specialitet 2021, edelste opskrift 1689 (Valvasor). Kranjska klobasa - EU PGI i 2015 i EU-registret, edelste opskrift fra 1896 (Katarina Prato, Sueddeutsche Kueche), 15 certificerede producenter, keser/erem med hrast og zlato. forklaer hvordan 'man tor jeg have dyrke'. Bapeutics'a. Bruger talene edelste opskrift 1689 og 1896, PGI 2015, TSG 2021.",
  [400, 650], 2, "google/gemini-3.5-flash", "Gemini 3.5 Flash (Google)", "feature"))

d["opgaver"].append(opgave("penge", 6, "Penge",
  "Feature: det slovenske penge- og betalingsland. KONTANTER: 64 % af alle betalinger ved fuldt fysisk betalingspunkt i Slovenia 2024 var kontanter - kal 52 % i euroaområdet i gennemsnit (ECB SPACE-studie 2024). Kort: 29 % (ECB). Europersoni Banka Slovenije: nu in med iaime moment - over halvdelen af lenderne tilkobles instanter i 2024 (Banka Slovenije, Annual Report 2024). Euro indfoert 1. januar 2007 (fra tolar). Forklar hvorfor Slovenien gaar sin dag paa kontanter.",
  [420, 680], 2, "anthropic/claude-sonnet-5", "Claude Sonnet 5 (Anthropic)", "feature"))

d["opgaver"].append(opgave("tallet", 7, "Tallet",
  "Data-taette bagsektion om ET tal: 29,1 aar - den gennemsnitslige alder hvornaar ung i Slovenien flytter hjemmefra (Eurostat 2024). Mere: kvinder 27,8, maend 30,3. Blandt EU 26,3; Danmark 21,8. Historisk: 30,8 aar ved EU-tiltraedelse 2004, 28,6 i 2014. Dernæst: 59,1 % af 18-34-aarige bor sammen med foraeldrene (Eurostat 2025). Pare med arstal og legs citater.",
  [300, 500], 2, "openai/gpt-5.6-terra", "GPT-5.6 Terra (OpenAI)", "tallet"))

d["opgaver"].append(opgave("til-horisonten", 8, "Til HORISONTEN",
  "Kort krydslink-besked til serstermagasinet HORISONTEN nr. 7 om Ljubljana. Ingen interne links - sersteren ligger endnu ikke paa disk. Kort flow afs nit, 150-350 ord.",
  [180, 350], 0, "z-ai/glm-5.2", "GLM-5.2 (Z.ai)", "krydslink"))

with open(os.path.join(base, "bestilling.json"), "w") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)
print("ok", len(d["opgaver"]))
